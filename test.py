# JUST FOR TEST
from src.utils import load_object
from src.exception import CustomException
import sys
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline





preprocessor_path = 'artifacts/preprocessor.pkl'
preprocessor = load_object(file_path=preprocessor_path)

data = CustomData(
    gender= np.nan,
    race_ethnicity=np.nan,
    parental_level_of_education=np.nan,
    lunch=np.nan,
    test_preparation_course=np.nan,
    reading_score=np.nan,
    writing_score=np.nan  
)

pred_df=data.get_data_as_data_frame()

data_scaled = preprocessor.transform(pred_df)

#onehot_values = preprocessor.transform(np.array([np.nan, np.nan, 'M','as','asa','asa','zxz']))
print(data_scaled)
