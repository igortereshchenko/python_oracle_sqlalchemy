import cx_Oracle
from sqlalchemy import create_engine
from dao.credentials import *
from sqlalchemy.orm import sessionmaker

class OracleDb(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                connection = cx_Oracle.connect(username, password, "{0}:{1}/{2}".format(host,port,service))
                cursor = connection.cursor()

                cursor.execute('SELECT * FROM v$version')
                db_version = cursor.fetchone()

                print("New connection to {} created".format(db_version[0]))

                oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

                engine = create_engine(
                    oracle_connection_string.format(
                        username=username,
                        password=password,
                        hostname=host,
                        port=port,
                        database=service,
                    )
                )

                Session = sessionmaker(bind=engine)
                session = Session()

                OracleDb._instance.connection = connection
                OracleDb._instance.cursor = cursor
                OracleDb._instance.sqlalchemy_session = session
                OracleDb._instance.sqlalchemy_engine = engine

            except Exception as error:
                print('Error: connection not established {}'.format(error))

        else:
            print('Connection already established')

        return cls._instance


    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor
        self.sqlalchemy_session = self._instance.sqlalchemy_session
        self.sqlalchemy_engine = self._instance.sqlalchemy_engine


    def execute(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        self.sqlalchemy_session.close()



if __name__=="__main__":
    db = OracleDb()
    db = OracleDb()
    db = OracleDb()
    db = OracleDb()
