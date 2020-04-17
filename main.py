# imports
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json', 'r') as c:
    params = json.load(c)['params']

local_server = params['local_server']
app = Flask(__name__)
app.secret_key = 'woret3@$%33gh5ffvv99%/dnggmbbb'

# database connectivity
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
        user='root', password='', server='localhost', database='otmess')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_username']:
        silver = silver_info.query.all()
        platinum = platinum_info.query.all()
        gold = gold_info.query.all()
        return render_template('admin_home.html', silver=silver, platinum=platinum, gold=gold)
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')
        if username == params['admin_username'] and password == params['admin_password']:
            session['user'] = username
            silver = silver_info.query.all()
            platinum = platinum_info.query.all()
            gold = gold_info.query.all()
            return render_template('admin_home.html', silver=silver, platinum=platinum, gold=gold)
    return render_template('admin_login.html')


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/customer")
def admincustomer():
    if 'user' in session and session['user'] == params['admin_username']:
        mess_cart = mess_cart_information.query.all()
        return render_template('admn_customer.html', mess_cart=mess_cart)
    else:
        return render_template('admin_login.html')


class silver_info(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(40), nullable=False)
    breakfast = db.Column(db.String(10), nullable=False)
    lunch = db.Column(db.String(40), nullable=False)
    dinner = db.Column(db.String(20), nullable=False)


class platinum_info(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(40), nullable=False)
    breakfast = db.Column(db.String(10), nullable=False)
    lunch = db.Column(db.String(40), nullable=False)
    dinner = db.Column(db.String(20), nullable=False)


class gold_info(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(40), nullable=False)
    breakfast = db.Column(db.String(10), nullable=False)
    lunch = db.Column(db.String(40), nullable=False)
    dinner = db.Column(db.String(20), nullable=False)


@app.route("/mess")
def messcart():
    silver = silver_info.query.all()
    platinum = platinum_info.query.all()
    gold = gold_info.query.all()
    return render_template('mess_page.html', silver=silver, platinum=platinum, gold=gold)


class mess_cart_information(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    mess_name = db.Column(db.String(40), nullable=False)
    mess_phone_no = db.Column(db.String(10), nullable=False)
    mess_address = db.Column(db.String(40), nullable=False)
    mess_offer_type_selected = db.Column(db.String(20), nullable=False)
    mess_price = db.Column(db.String(8), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/mess_form", methods=['GET', 'POST'])
def mess():
    greeting = "thankyou for ordering our mess service we will call you back for conformation"
    # name,phone_no, address,offer_type_selected,price
    if request.method == 'POST':
        mess_name = request.form.get('mess_cart_name')
        mess_phone = request.form.get('mess_cart_phone_no')
        mess_address = request.form.get('mess_cart_address')
        mess_offer_selected = request.form.get('offer')
        mess_total_price = request.form.get('jsonitem')
        entry = mess_cart_information(mess_name=mess_name, mess_phone_no=mess_phone, mess_address=mess_address,
                                      mess_offer_type_selected=mess_offer_selected, mess_price=mess_total_price,
                                      date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return render_template('thankyou.html', greet=greeting)

    return render_template('mess_form.html')


class contact_information(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(5000), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    greeting = "thankyou for your Feedback"
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = contact_information(name=name, email=email, phone_no=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return render_template('thankyou.html', greet=greeting)

    return render_template('contact_us.html')


@app.route("/about")
def about():
    return render_template('about_us.html')


app.run(debug=True)
