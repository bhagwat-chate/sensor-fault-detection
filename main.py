from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig

if __name__=="__main__":
    mongodb_client = MongoDBClient()
    print("collection name: ", mongodb_client.database.list_collection_names())

    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)

    print("Training pipeline: ", training_pipeline_config.__dict__)
    print("Data Ingestion Pipeline: ", data_ingestion_config.__dict__)

