import os, sys
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging

# from sensor.configuration.mongo_db_connection import MongoDBClient
# from sensor.utils.main_utils import read_yaml_file
#
# from fastapi import FastAPI
# from sensor.constant.application import APP_HOST, APP_PORT
# from starlette.responses import RedirectionResponse
# from unicorn import run as app_run
# from fastapi.responses import Response
#
# def set_env_variable(env_file_path):
#     env_config = read_yaml_file(env_file_path)
#     os.environ["MONGO_DB_URL"]=env_config["MONGO_DB_URL"]
#
# env_file_path = "config/workspace/env.yaml"
# set_env_variable(env_file_path)
#
# @app.get("/", tags=['authentication'])
# async def index():
#     return RedirectionResponse(url="docs")
#
# @app.get("/train")
# async def trainRouteClient():
#     try:
#         train_pipeline = TrainPipeline()
#         train_pipeline.run_pipeline()
#
#         return Response("Training successful!")
#     except Exception as e:
#         return Response(f"Error occurred! {e}")

if __name__=="__main__":

    try:

        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        logging.info("training complete")

    except Exception as e:
        print(e)
        logging.exception(e)
