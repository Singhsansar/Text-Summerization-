from TextSummerizer.components.model_trainer import ModelTrainer
from TextSummerizer.config.configuration  import ConfigurationManager
from TextSummerizer.logging import logger 


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config  = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e: 
            raise e 
