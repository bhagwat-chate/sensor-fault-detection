import os
from datetime import datetime
from sensor.constant.training_pipeline import ARTIFACT_DIR, DATA_INGESTION_COLLECTION_NAME
from sensor.constant.training_pipeline import PIPELINE_NAME, DATA_INGESTION_DIR_NAME, DATA_INGESTION_FEATURE_STORE_DIR
from sensor.constant.training_pipeline import DATA_INGESTION_INGESTED_DIR, FILE_NAME, TRAIN_FILE_NAME, TEST_FILE_NAME
from sensor.constant.training_pipeline import DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
from sensor.constant import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp



class DataIngestionConfig:
    def __init__(self, training_pipeline_config):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
        self.training_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
        self.testing_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
        self.train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = DATA_INGESTION_COLLECTION_NAME








