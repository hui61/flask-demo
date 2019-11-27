from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, request, session
import config
from db import db
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config.from_object(config)
Swagger(app)
db.init_app(app)


@app.route('/')
def index():
    return 'Please try http://127.0.0.1:12000/apidocs/ to call api'


@app.route('/api/login', methods=['POST'])
@swag_from('yml/login.yml')
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        user = User.query.filter(User.name == user_name, User.password == user_password).first()
        if user is not None:
            session['user_id'] = user.id
            session['user_role'] = user.role
            return 'Successfully'
        else:
            return 'Unsuccessfully'


@app.route('/api/user/<user_id>', methods=['GET'])
@swag_from('yml/query.yml')
def query(user_id):
    if user_id is None:
        users = User.query.all()
        user_string = ''
        for user in users:
            user_string = user.__repr__() + '\n' + user_string
        return user_string
    else:
        user = User.query.filter(User.id == user_id).first()
        return user.__repr__()


@app.route('/api/user/', methods=['POST'])
@swag_from('yml/insert.yml')
def insert():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        user_role = request.form['user_role']
        user = User(name=user_name, password=user_password, role=user_role)
        db.session.add(user)
        db.session.commit()
        return user.__repr__() + ' add successfully'


@app.route('/api/user/<user_id>', methods=['PUT'])
@swag_from('yml/edit.yml')
def edit(user_id):
    if request.method == 'PUT':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        user_role = request.form['user_role']
        update_status = User.query.filter(User.id == user_id).update(
            {'name': user_name, 'password': user_password, 'role': user_role})
        db.session.commit()
        return update_status.__repr__()


@app.route('/api/user/<user_id>', methods=['DELETE'])
@swag_from('yml/delete.yml')
def delete(user_id):
    if request.method == 'DELETE':
        delete_status = User.query.filter(User.id == user_id).delete()
        db.session.commit()
        return delete_status.__repr__()


@app.before_request
def auth_required():
    if request.path != '/':
        if request.path != '/api/login':
            if request.path != '/apidocs/':
                if 'flasgger' not in request.path:
                    if 'apispec_1.json' not in request.path:
                        if 'user_id' not in session:
                            return 'Need login'
                        else:
                            user_role = session['user_role']
                            if user_role == 0:
                                return 'Your are not admin'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
