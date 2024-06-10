from flask import Flask,request

app=Flask(__name__)

#%%
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/home")
def homepage():
    return "<h1>homepage</h1>"

#import  controller.user_controller as user_controller
#import  controller.product_controller as product_controller
#%%
#from controller import product_controller,user_controller

from controller import *

