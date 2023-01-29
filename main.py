from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.entity.config_entity import TrainingPipelineConfig
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.config_entity import DataValidationConfig
from sensor.entity.config_entity import DataTransformationConfig

if __name__=="__main__":

    try:

        # mongodb_client = MongoDBClient()
        # print("collection name: ", mongodb_client.database.list_collection_names())

        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        # print("Training pipeline: ", training_pipeline_config.__dict__)
        # print("Data Ingestion Pipeline: ", data_ingestion_config.__dict__)

        # data_validation_config = DataValidationConfig(training_pipeline_config)
        # print("Data validation configuration: ", data_validation_config.__dict__)

        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        print("Data Transformation Config: ", data_transformation_config.__dict__)


        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

    except Exception as e:
        print(e)