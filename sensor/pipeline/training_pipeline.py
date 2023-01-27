from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.components.data_ingestion import DataIngestion
from sensor.exception import SensorException
from sensor.logger import logging
import sys


class TrainPipeline:

    def __init__(self):
        training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion complete and artifact: {data_ingestion_artifact}")
            logging.info("Data ingestion complete")

            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def start_data_validation(self):
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def start_data_transformation(self):
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def start_model_trainer(self):
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def start_model_evaluation(self):
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def start_model_pusher(self):
        try:
            pass

        except Exception as e:
            raise SensorException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()

        except Exception as e:
            raise SensorException(e, sys)
