from src.datascience.config.configuration import DataValidationMgr
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        mgr = DataValidationMgr()
        config = mgr.get_data_validation_config()
        entity = DataValidation(config=config)
        entity.validation_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f'>>> stage {STAGE_NAME} started <<<')
        obj = DataValidationTrainingPipeline()
        obj.main ()
        logger.info(f'>>> stage {STAGE_NAME} completed <<<\n')
    except Exception as e:
        logger.exception(e)
        raise e