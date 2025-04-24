from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    # print logs
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    # define pipline Object
    obj = DataIngestionTrainingPipeline()
    obj.main()
    # log output
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")
except Exception as e:
    logger.exception(e)
    raise e