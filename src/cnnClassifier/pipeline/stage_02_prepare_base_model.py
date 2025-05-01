from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare base model"

# define Data ingestion training pipeline
class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # define Configuration Manager
        config = ConfigurationManager()
        # Get config of model preperation
        prepare_base_model_config = config.get_prepare_base_model_config()
        # prepare base model
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        # get base model
        prepare_base_model.get_base_model()
        # save base model
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        # print logs
        logger.info(f"****************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # define pipline Object
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        # log output
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")
    except Exception as e:
        logger.exception(e)
        raise e