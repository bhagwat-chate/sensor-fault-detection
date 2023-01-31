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
from sensor.entity.config_entity import ModelEvaluationConfig, ModelPusherConfig
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model import SensorModel
from sensor.ml.model.estimator import ModelResolver

import os, sys

class ModelPusher:
    def __init__(self, model_pusher_config:ModelPusherConfig, model_eval_artifact:ModelEvaluationArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = self.model_eval_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_modelpusher(self):
        pass
