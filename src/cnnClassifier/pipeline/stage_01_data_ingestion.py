from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion Stage"

# define Data ingestion training pipeline
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # define Configuration Manager
        config = ConfigurationManager()
        # Get config of data ingestions
        data_ingestion_config = config.get_data_ingestion_config()
        # define data ingestion object
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # download the data
        data_ingestion.download_file()
        # unzip the data
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
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