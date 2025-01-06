from operator import itemgetter
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

class DatabaseSessionProvider:
    def __init__(self, config: dict):
        self.__connection_string = self.__get_connection_string(config=config)
        self.__engine = create_engine(self.__connection_string)
        self.__session = None

        self.__initialize_session()

    def __get_connection_string(self, config: dict):
        user_name, password, name, host, port = \
            itemgetter(
                'DATABASE_USERNAME',
                'DATABASE_PASSWORD',
                'DATABASE_NAME',
                'DATABASE_HOST',
                'DATABASE_PORT'
            )(config)
        return f"postgresql://{user_name}:{password}@{host}:{port}/{name}"

    def __initialize_session(self):
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def __dispose_and_recreate_engine(self):
        self.__engine.dispose()
        self.__engine = create_engine(self.__connection_string)

    def get_session(self):
        try:
            self.__session.execute(text('SELECT 1'))
        except OperationalError:
            self.__dispose_and_recreate_engine()
            self.__initialize_session()

        return self.__session
