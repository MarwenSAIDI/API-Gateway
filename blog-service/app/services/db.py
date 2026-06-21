from sqlmodel import create_engine, SQLModel, Session
from app.config import config

class Database:
    def __init__(self, database_url:str = config.DATABASE_URI):
        self.engine = create_engine(
            url=database_url,
            connect_args={
                "check_same_thread": False
            }
        )

        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            yield session

database = Database(
    database_url=config.DATABASE_URI,
)