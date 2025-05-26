from sqlmodel import create_engine, Session
from llmbuddy.constants import SQLALCHEMY_DATABASE_URL

connection_args = {"check_same_thread" : False}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connection_args)

def get_session():
    with Session(engine) as session: 
        yield session