from bson import ObjectId


# Function to convert ObjectId to string recursively
def convert_objectid_to_string(doc):
    if isinstance(doc, dict):
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, dict) or isinstance(value, list):
                convert_objectid_to_string(value)
    elif isinstance(doc, list):
        for item in doc:
            convert_objectid_to_string(item)
