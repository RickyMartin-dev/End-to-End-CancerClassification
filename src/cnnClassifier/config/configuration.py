from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig)

# Create Configuration Manager
class ConfigurationManager:
    def __init__(self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # Read Yaml files from config and params
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Run the create directories python script
        create_directories([self.config.artifacts_root]) # creates artifacts/

    # Data Ingestions Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Run the create directories python script
        create_directories([config.root_dir]) # creates artifacts/data_ingestion/

        # Data Ingestions Config
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config