from flask import Blueprint

main = Blueprint('users', __name__)

@main.route('/')
def get_user():
    return {'message': 'Users'}
