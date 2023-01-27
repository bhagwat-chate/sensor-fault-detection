import os.path
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData
from sensor.constant.database import DATABASE_NAME
from sensor.constant.database import COLLECTION_NAME
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import sys


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def export_data_into_feature_store(self) -> DataFrame:
        """
              Export mongo db collection record as data frame into feature
        """
        try:
            logging.info("Exporting data from mongodb to feature store")
            sensor_data = SensorData()
            collection_name: str = COLLECTION_NAME
            dataframe = sensor_data.export_collection_as_dataframe(collection_name)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except  Exception as e:
            raise e

    def split_train_test_split(self, dataframe: DataFrame)-> None:
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("performed train, test split on the dataframe")
            logging.info("Exited train_test_split of the data_ingestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info("Exporting train and test file path")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info("Exported train and test file path")
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_train_test_split(dataframe=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except SensorException as e:
            raise e