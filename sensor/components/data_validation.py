from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.artifact_config import DataValidationArtifact
from sensor.entity.config_entity import DaraValidationConfig
from sensor.exception import SensorException
from senslor.logger import logging
import pandas as pd
import os, sys
from sensor.utils.main_yaml import read_yaml_file, write_yaml_file
class DataValidation:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e, sys)

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            number_of_columns = self._schema_config['columns']
            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e, sys)

    def drop_zero_std_columns(self, dataframe: DataFrame) -> pd.DataFrame:
        pass

    def is_numerical_column_exist(self, dataframe: pd.DataFrame) -> bool:
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            numerical_column_present = True
            missing_numerical_column = []
            for col in dataframe.columns:
                if col not in numerical_columns:
                    numerical_column_present = False
                    missing_numerical_column.append(col)

            logging.info(f"Missing numerical columns: [{missing_numerical_column}]")
            return numerical_column_present
        except Exception as e:
            raise SensorException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            dataframe = pd.read_csv(file_path)
            return dataframe
        except Exception as e:
            raise SensorException(e, sys)

    def detect_data_drift(self):
        pass

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            error_message = ""
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data from train, test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of column
            status = self.validate_number_of_columns(train_dataframe)
            if not status:
                error_message = f"{error_message} train dataframe does not contain all columns"
            else:
                error_message = f"{error_message} train dataframe contain all columns"

            error_message = ""
            test = self.validate_number_of_columns(test_dataframe)
            if not status:
                error_message = f"{error_message} test dataframe does not contain all the columns"
            else:
                error_message = f"{error_message} test dataframe contain all the columns"


            # Validate numerical columns
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all the numerical columns"

            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test dataframe does not contain all the numerical columns"

            if len(error_message) > 0:
                raise Exception(error_message)


            # Data Drift


        except Exception as e:
            raise(e, sys)

