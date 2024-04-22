from typing import Any, Dict

from bson import ObjectId
from pydantic import BaseModel
from pydantic_core import core_schema


class PyObjectId(str):
    """
    Custom type for ObjectId, which is a 12-byte identifier for MongoDB documents.
    This type is used to validate and serialize ObjectId values in Pydantic models.
    https://stackoverflow.com/questions/76686888/using-bson-objectid-in-pydantic-v2/77105412#77105412
    """

    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(cls.validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x)
            ),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        """
        Validates the ObjectId value.
        """
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)


from pydantic_core import core_schema


def to_mongo_compatible_dict(model: BaseModel) -> Dict[str, Any]:
    """
    Convert a Pydantic model to a dictionary compatible with MongoDB insertions
    while preserving ObjectId types.
    """
    output = {}
    for field_name, field_value in model:
        if hasattr(field_value, "dict"):
            # Recursive call for nested models
            output[field_name] = to_mongo_compatible_dict(field_value)
        elif isinstance(field_value, (PyObjectId, ObjectId)):
            # Directly use ObjectId without conversion
            output[field_name] = ObjectId(str(field_value))
        else:
            output[field_name] = field_value
    return output
