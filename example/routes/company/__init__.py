from flask import Blueprint

main = Blueprint('companies', __name__)

@main.route('/')
def get_user():
    return {'message': 'companies'}
