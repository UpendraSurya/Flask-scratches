import sqlite3
import json
from flask import request,make_response

class UserModel:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('user_model.db', check_same_thread=False)
            # why do we use cursor?
            # it allows you go through the content of the database
            self.cursor = self.conn.cursor()
            print("Connection established")
            self.create_table()
        except sqlite3.Error as e:
            print(f"Connection failed: {e}")
            self.conn = None

    def create_table(self):
        if self.conn is None:
            return
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )
            ''')
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(f"Failed to create table: {e}")

    def insert_user(self,data):
        #this part is used for inserting the data into the database.
        self.cursor.execute(f"INSERT INTO users(name,age) VALUES ('{data['name']}','{data['age']}')")
        print (data)
        self.conn.commit()
        return "user created successfully"

    def update_user(self,data):
        #this part of the code is used for updating the already present user
        self.cursor.execute(f"UPDATE users SET name='{data['name']}',age='{data['age']}' WHERE id={data['id']}")
        self.conn.commit()
        return "user updated successfully"

    def delete_user(self,id):
        self.cursor.execute(f"DELETE FROM users WHERE id= ?  ",(id,))
        self.conn.commit()
        if self.cur.rowcount > 0:
            return make_response({"message":"user deleted successfully"} , 201)
        else:
            return make_response({"message": "Nothing to delete"} , 202)

    def user_getall_model(self):
        if self.conn is None:

            return None
        try:
            # This is one of the CURD operation that is Read.
            self.cursor.execute('SELECT * FROM users')
            # to fetch the data from the database
            self.rows = self.cursor.fetchall()
            print("done")
            print(self.rows)
            return json.dumps (self.rows)#this json fuction lets as to view the values on the web as string
            return "this page is ready for viewing"
        except sqlite3.Error as e:
            print(f"Failed to retrieve users: {e}")
            return None

    def close_connection(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Connection closed")

#%%

#%%
