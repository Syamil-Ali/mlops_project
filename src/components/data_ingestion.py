# Data Ingestion 
# -- Responsible for reading data

import os
import sys 

#reason is to handle exception
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #use to create class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv') #save train csv in the artifacts folder
    test_data_path: str=os.path.join('artifacts', 'test.csv') #save train csv in the artifacts folder
    raw_data_path: str=os.path.join('artifacts', 'data.csv') #save train csv in the artifacts forlder

# reason why make the folder here
# so that data ingestion know where to save all the file (maybe explaination for beginner like me TT)


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # initialize the data ingestion config


    def initiate_data_ingestion(self): # initiate the data ingestion 
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # create the directory with condition if the directory already exist then no need to create back the folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test splot initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


# test the code
if __name__ == "__main__":

    obj = DataIngestion()
    #obj.initiate_data_ingestion()

    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)





