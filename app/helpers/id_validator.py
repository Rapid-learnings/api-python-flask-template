from bson import ObjectId


def is_valid_objectid(s):
    try:
        ObjectId(s)
        return True
    except Exception:
        return False
