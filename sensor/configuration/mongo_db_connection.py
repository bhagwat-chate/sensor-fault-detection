import os
import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.database import COLLECTION_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
from sensor.logger import logging
from sensor.exception import SensorException
import os, sys
ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME, collection_name=COLLECTION_NAME)-> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except SensorException as e:
            raise SensorException(e, sys)
