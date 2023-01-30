from sensor.utils.main_utils import load_numpy_array_data
from sensor.utils.main_utils import save_object
from sensor.utils.main_utils import load_object
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.entity.artifact_entity import DataValidationArtifact
from sensor.entity.artifact_entity import ModelEvaluationArtifact
from sensor.entity.artifact_entity import DataTransformationArtifact
from sensor.entity.artifact_entity import ModelTrainerArtifact
from sensor.entity.config_entity import ModelEvaluationConfig
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model import SensorModel
from sensor.ml.model.estimator import ModelResolver

import pandas as pd
import os, sys

class ModelEvaluation:
    def __init__(self, model_eval_config:ModelEvaluationConfig,
                 data_validation_artifact:DataValidationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact
                 ):
        try:
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path - self.data_validation_artifact.valid_test_file_path

            # Valid train, test file
            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)

            pd.concat([train_df, test_df], axis=)
            train_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model_resolver = ModelResolver()

            is_model_accecpted = True
            if not model_resolver.is_model_exists():
                model_evaluation_artifact = ModelEvaluationArtifact(is_model_accecpted=is_model_accecpted,
                                                                    improved_accuracy=None,
                                                                    best_model_path=None,
                                                                    trained_model_path=train_model_file_path,
                                                                    train_model_metric_artifact=self.model_trainer_artifact.test_metric_artifact,
                                                                    best_model_metric_artifact=None)

                logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")
                return model_evaluation_artifact

            latest_model_path = model_resolver.get_best_model_path()
            latest_model = load_object(file_path=latest_model_path)
            train_model = load_object(file_path=train_model_file_path)

        except Exception as e:
            raise SensorException(e, sys)