from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_htmx import HTMX
from flask_wtf.csrf import CSRFProtect
from models import *

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/guard_dog'
app.config['SECRET_KEY'] = 'YOUR SECRET KEY HERE'
mongo = PyMongo(app)
htmx = HTMX(app)
csrf = CSRFProtect(app)



@app.route('/')
def index():
    return render_template('index.j2')

@app.route('/sign-in')
def sign_in():
    pass

@app.route('/accounts')
def accounts():
    return render_template('accounts.j2', title='Accounts')

@app.route('/personal-info', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        img = request.form.get('img')
        name = request.form.get('name')
        email = request.form.get('email')
        personal_info = mongo.db.accounts.insert_one({'name' : name, 'email' : email, 'profile_image' : img})
        #return render_template('')
    return render_template('personal_info.j2', title='Personal Info')

@app.route('/notes')
def notes():
    return render_template('notes.j2', title='Notes')

@app.route('/password-generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        password_generator = PasswordGenerator(length=int(request.form.get('password_length')), characters=str(request.form.get('password_characters')))
        return render_template('password_generator.j2', title='Password generator',password=password_generator.generate_password() )
    return render_template('password_generator.j2', title='Password generator')

if __name__ == '__main__':
    app.run(debug=True)