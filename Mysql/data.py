from mysql.connector import connect, Error
from . import query
import config

class Database():
    def __init__(self):
        self.query = query.Query()
        if config.STARTED:
            self.connection = connect(
                host = config.HOST,
                user = config.USERNAME,
                password = config.PASSWORD,
                database = config.DATABASE
            )
        else:
            pass

    def setup(self, username, password, host):
        try:
            with connect(host = host, user = username, password = password) as connection:
                
                try:
                    with connection.cursor() as cursor:
                        for query in self.query.setup_queries:
                            print(query)
                            cursor.execute(query)
                        cursor.commit()
                except:
                    print('Error While creating tables.')
                    return
                
                config.file_write({'started': True})
        except Error as e:
            print(f'Connection Error. Error {e}')
            
            """
            Error GUI code.
            """
            return False
        # When everything right.
        return True

    def insert(self, table, data):
        i_query = self.query.insert(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.executemany(i_query, data)
                cursor.commit()
        except Error as e:
            print(f'Error {e}')
            """
            Error GUI code.
            """
            return False
        return True

    def update(self, table, data):
        u_query = self.query.update(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(u_query, data)
                cursor.commit()
        except Error as e:
            print(f'Error {e}')
            """
            Error GUI code.
            """
            return False
        return True

    def delete(self, table, data):
        d_query = self.query.delete(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(d_query, data)
                cursor.commit()
        except Error as e:
            print(f'Error {e}')
            """
            Error GUI code.
            """
            return False
        return True

    def select(self, table):
        s_query = self.query.select(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(s_query)
                return cursor.fetchall()
        except Error as e:
            print(f'Error {e}')
            """
            Error GUI code.
            """
            return False

    def select_where(self, table, data):
        s_query = self.query.select_where(table)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(d_query, data)
                return cursor.fetchall()
        except Error as e:
            print(f'Error {e}')
            """
            Error GUI code.
            """
            return False