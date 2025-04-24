import os
import sys  
import logging

# Define logging String
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# logging dirictory/file
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Logging Config
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# name/create log
logger = logging.getLogger("cnnClassifierLogger")