import sys
from typing import Optional
import numpy as np
import pandas as pd
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException
from sensor.logger import logging


class SensorData:
    """
    This class help to export entire MongoDB records as dataframe
    """
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except SensorException as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            Export entire collection as dataframe. Return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if '_id' in df.columns.to_list():
                df.drop(columns=['_id'], axis=1, inplace=True)

            df.replace({"na": np.nan}, inplace=True)

            return df
        except Exception as e:
            raise SensorException(e, sys)