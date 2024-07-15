# import mysql.connector
# from mysql.connector import Error

# class MySQLDatabase:
#     def __init__(self, host, database, user, password):
#         self.host = host
#         self.database = database
#         self.user = user
#         self.password = password
#         self.connection = None
#         self.cursor = None
#         self.connect()

#     def connect(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password
#             )
#             if self.connection.is_connected():
#                 db_info = self.connection.get_server_info()
#                 print(f"Connected to MySQL Server version {db_info}")
#                 self.cursor = self.connection.cursor()
#                 self.cursor.execute("select database();")
#                 record = self.cursor.fetchone()
#                 print(f"You're connected to database: {record}")
#         except Error as e:
#             print(f"Error while connecting to MySQL: {e}")

#     def execute(self, query):
#         try:
#             self.cursor.execute(query)
#             self.connection.commit()
#             print("Query executed successfully")
#         except Error as e:
#             print(f"Error while executing query: {e}")

#     def retrieve_table(self, table_name):
#         try:
#             self.cursor.execute(f"SELECT * FROM `{table_name}`")
#             rows = self.cursor.fetchall()
#             return rows
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
#     def retrieve_id(self, table_name,id):
#         try:
#             self.cursor.execute(f"SELECT * FROM `{table_name}` WHERE `id`={id}")
#             rows = self.cursor.fetchall()
#             return rows
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
#     def rsa(self, table_name,id,date):
#         try:
#             self.cursor.execute(f"SELECT * FROM `{table_name}` WHERE `id`={id} AND `date`='{date}'")
#             rows = self.cursor.fetchall()
#             return rows
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
#     def insert_to_attendance_log(self,values):
#        # ('23', 'sdasd', '08:30:16', '2024-06-05')

#         try:
#             self.cursor.execute(f"SELECT * FROM `attendance_log` WHERE `id`='{values[3]}' AND `date`='{values[2]}'")
#             rows = self.cursor.fetchall()
#             if rows:
#                 print("double login detected!!!!")
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
        
#         query=f"INSERT INTO `attendance_log` (`id`,`name`, `time`, `date`) VALUES {values};"
#         try:
#             self.execute(query)
#             print("executed")
#             return True
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
        
#     def retrieve_todays_attendance(self, table_name,date):
#         try:
#             print(date)
#             self.cursor.execute(f"SELECT * FROM `{table_name}` WHERE `date`='{date}'")
#             rows = self.cursor.fetchall()
#             return rows
#         except Error as e:
#             print(f"Error while retrieving table: {e}")
#             return None
#     def close(self):
#         if self.connection.is_connected():
#             self.cursor.close()
#             self.connection.close()
#             print("MySQL connection is closed")

# # Example usage:
# if __name__ == "__main__":
#     print("please run serve.py")
   
import sqlite3

class MySQLDatabase:
    def __init__(self,database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def retrieve_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def retrieve_id(self, table_name, id):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id={id}")
        return self.cursor.fetchone()

    def retrieve_todays_attendance(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def rsa(self, table_name, id, date):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id={id} AND date='{date}'")
        return self.cursor.fetchone()

    def insert_to_attendance_log(self, value):
        self.cursor.execute(f"INSERT INTO attendance_log (id, name, time, date) VALUES {value}")
        self.conn.commit()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()

print(MySQLDatabase("amms.db").retrieve_todays_attendance("attendance_log"))