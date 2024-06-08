import sqlite3
class user_model():
    def __init__(self):
        # connection establishment code for db
        try:
            nnect=sqlite3.connect('user_model.db')
            cursor=nnect.cursor()
            print("Connection established")
        except :
            print("Connection failed")
    def user_getall_model(self):
        return "This is user sign model"