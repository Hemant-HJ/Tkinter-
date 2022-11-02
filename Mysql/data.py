from mysql.connector import connect, Error
from . import query
import config

class Database():
    def __init__(self):
        self.query = query.Query()
        if config.STARTED:
            self.connection = connect(host = config.HOST, user = config.USERNAME, password = config.PASSWORD,
                port = config.PORT, database = config.DATABASE)
    def setup(self, username, password, host, port = 3306):
        try:
            with connect(host = host, user = username, password = password, port = port) as connection:
                
                try:
                    with connection.cursor() as cursor:
                        for query in self.query.setup_queries:
                            print(query)
                            cursor.execute(query)
                        connection.commit()
                except Error as e:
                    print(f'Error While creating tables.{e}')
                    return
        except Error as e:
            return False
        return True

    def insert(self, table, data):
        print(table)
        i_query = self.query.insert(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(i_query, data)
                self.connection.commit()
        except Error as e :
            print(f'Error {e}')
            return e
        return True

    def update(self, table, data):
        u_query = self.query.update(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(u_query, data)
                self.connection.commit()
        except Error as e:
            print(f'Error {e}')
            return False
        return True

    def delete(self, table, data):
        d_query = self.query.delete(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(d_query, [data])
                self.connection.commit()
        except Error as e:
            print(f'Error {e}')
            return e
        return True

    def select(self, table):
        s_query = self.query.select(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(s_query)
                return cursor.fetchall()
        except Error as e:
            print(f'Error {e}')
            return e