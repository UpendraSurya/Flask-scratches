from app import app
from model.user_model import user_model
usermodel = user_model()
@app.route('/user/getall')
def usergetall():
    return usermodel.user_getall_model()