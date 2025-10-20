import pymongo

from userbot import DB_NAME, IS_ATLAS, MONGO_URL


def database():
    """Created Database connection"""
    if IS_ATLAS:
        client = pymongo.MongoClient(
            MONGO_URL,
        )
    else:
        from userbot import DB_PASSWORD, DB_USERNAME

        client = pymongo.MongoClient(
            MONGO_URL, username=DB_USERNAME, password=DB_PASSWORD
        )

    db = client[DB_NAME]
    return db
