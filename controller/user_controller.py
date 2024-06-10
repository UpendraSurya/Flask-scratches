from app import app
from flask import request
from model.user_model import UserModel
usermodel = UserModel()
@app.route('/user/getall')
def get_all():
     return usermodel.user_getall_model()
#%%

#%%
@app.route('/user/add', methods=["POST"])
def add_user():
#request from lets you connect with the post man
     return usermodel.insert_user(request.form)
#%%
@app.route('/user/update', methods=["PUT"])
def update_user():
    return usermodel.update_user(request.form)

@app.route('/user/delete/<int:id>', methods=["DELETE"])
def delete_user():
     return usermodel.delete_user(request.form)