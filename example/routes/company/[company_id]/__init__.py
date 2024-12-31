from flask import Blueprint

main = Blueprint('company', __name__)

@main.route('/')
def get_user(company_id):
    return {'message': 'company ' + company_id}
