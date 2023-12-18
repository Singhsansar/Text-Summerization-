import os
from TextSummerizer.entity import DataValidationConfig 
from TextSummerizer.logging import logger

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config


    def validate_all_files_exists(self)-> bool:
        try: 
            validation_status = True
#-/artifacts/data_ingestion/Textsummarizer_BCC_dataset
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","Textsummarizer_BCC_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES: 
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f :
                        f.write(f"validation status:{validation_status}")
                else: 
                    validation_status = True 
                    with open (self.config.STATUS_FILE,'w') as f: 
                        f.write(f"validation status:{validation_status}")

            return validation_status
        
        except Exception as e :
            raise e 