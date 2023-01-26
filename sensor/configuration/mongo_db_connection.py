import os
import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.database import COLLECTION_NAME
from sensor.constant.database import USER_NAME
from sensor.constant.database import PASSWORD
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME, collection_name=COLLECTION_NAME, user_name=USER_NAME, password=PASSWORD)-> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://{v1}:{v2}@cluster0.q06oiaw.mongodb.net/?retryWrites=true&w=majority".format(v1=user_name, v2=password)
                # mongo_db_url = os.getenv(MONGODB_URL_KEY)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
