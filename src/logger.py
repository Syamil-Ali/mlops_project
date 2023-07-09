# purpose
# use to store every execution, information running into one file
# for tracking purpose

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) 
# 1. get current working directory of the python run (not the file run)
# 1.1 lets say if python run from the mlops project file, 
# --> mlops is the cwd
# 2. join the log file

os.makedirs(logs_path, exist_ok=True) # create the directory

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


# create format for the log
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format =  "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, # has many (can check documentation), but .INFO is just level for general information
)


# test logger
# if __name__== "__main__":
#     logging.info("Logging has started")