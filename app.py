from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_htmx import HTMX
from flask_wtf.csrf import CSRFProtect
from models import *
from datetime import datetime
import uuid

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

@app.route('/add/account/<id: uuid>')
def add_account():
    if request.method == 'POST':
        name = request.form.get('name')
        last_used = request.form.get('email')
        password = request.form.get('password')
        category = request.form.get('category') 
        image = request.form.get('image')
        uuid = request.form.get('uuid')
        #date_last_used = datetime.datetime.utcnow()
        #password_quality = Utilities.detect_password_quality(request.form.get('password'))
        accounts = { '$set' : {
                'name' : name, 
                'last_used' : '', 
                'password' : password,
                'category' : category,
                'image' : '',
                'password_quality' : '',
            }} 
        mongo.db.accounts.update_one({'uuid' : uuid}, 'accounts')
    return render_template('accounts.j2', title='Accounts')



@app.route('/personal-info', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        profile_image = request.form.get('profile_image')
        mongo.db.accounts.insert_one({'name' : name, 'email' : email, 'profile_image' : profile_image})
    return render_template('personal_info.j2', title='Personal Info')


@app.route('/notes')
def notes():
    return render_template('notes.j2', title='Notes')

@app.route('/add/notes/<id: uuid>')
def add_notes():
    if request.method == 'POST':    
        title = request.form.get('title')
        category = request.form.get('category')
        date_added = datetime.datetime.utcnow()
        priority = request.form.get('priority')
        notes = { '$set' : { 
            'title' : title,
            'category' : category,
            'date_added' : date_added,
            'priority' : priority
        }}
        mongo.db.accounts.update_one({'uuid' : uuid}, notes)

    return render_template('notes.j2', title='Notes')


@app.route('/password-generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        password_generator = PasswordGenerator(length=int(request.form.get('password_length')), characters=str(request.form.get('password_characters')))
        return render_template('password_generator.j2', title='Password generator', password=password_generator.generate_password() )
    return render_template('password_generator.j2', title='Password generator')




if __name__ == '__main__':
    app.run(debug=True)