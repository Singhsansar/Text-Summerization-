from TextSummerizer.components.data_validation import DataValidation
from TextSummerizer.config.configuration  import ConfigurationManager
from TextSummerizer.components.data_ingestion import DataIngestion
from TextSummerizer.logging import logger 


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exists()
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise