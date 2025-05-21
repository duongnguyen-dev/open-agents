from loguru import logger
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from databases.models import Models

class ModelService():
    def __init__(self, session) -> None:
        self.session = session

    def list_models(self):
        try: 
            query = select(Models)
            result = self.session.exec(query)
            logger.info("Query all models successfully!")
            
            return result
        except SQLAlchemyError as e:
            logger.error(e)
            return None