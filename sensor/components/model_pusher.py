from sensor.utils.main_utils import load_numpy_array_data
from sensor.utils.main_utils import save_object
from sensor.utils.main_utils import load_object
from sensor.utils.main_utils import write_yaml_file
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.artifact_entity import DataValidationArtifact
from sensor.entity.artifact_entity import ModelEvaluationArtifact
from sensor.entity.artifact_entity import DataTransformationArtifact
from sensor.entity.artifact_entity import ModelTrainerArtifact
from sensor.entity.artifact_entity import ModelPusherArtifact
from sensor.entity.config_entity import ModelEvaluationConfig, ModelPusherConfig
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.data_access.sensor_data import SensorData
from sensor.ml.model.estimator import ModelResolver
import shutil
import os, sys

class ModelPusher:
    def __init__(self, model_pusher_config:ModelPusherConfig, model_eval_artifact:ModelEvaluationArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_path

            # Creating model pusher dir to save model
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)

            shutil.copy(src=trained_model_path, dst=model_file_path)

            # saved model dir
            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            # prepare artifact
            model_pusher_artifact = ModelPusherArtifact(saved_model_path=saved_model_path, model_file_path=model_file_path)

            return model_pusher_artifact

        except Exception as e:
            raise SensorException(e, sys)
