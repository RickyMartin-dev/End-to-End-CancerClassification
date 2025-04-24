import os
import gdown
import zipfile

from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Fetch and download data From URL
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            # define URL and make data directories
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True) # create folder if need be
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Extract file ID and Download the zip file
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)

            # Log successful Downlad
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            # Raise Exception
            raise e

        
    # Unzip Data
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        # Unzip and read
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True) # create folder if need be
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)