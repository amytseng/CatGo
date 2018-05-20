from flask import Blueprint
from user.models import User

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    user = User(name='amytseng', password='1234', email='aammyytseng@gmail.com')
    user.save()
    return "Hello, {}!".format(user.name)
