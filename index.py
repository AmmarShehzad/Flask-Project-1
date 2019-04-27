from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contacts'
db = SQLAlchemy(app)

class contacts(db.Model):
    db = SQLAlchemy(app)
    sno = db.Column(db.Integer, primary_key=True)
    Phone = db.Column(db.String(13), unique= True , nullable = True)
    Email = db.Column(db.String(50), unique=False, nullable=True)

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/about")
def about():

    return render_template('about.html')


@app.route("/services")
def services():

    return render_template('services.html')


@app.route("/contact" , methods = ['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        phonenumber = request.form.get('phonenumber')
        email = request.form.get('email')
        entry=contacts(Phone = phonenumber , Email = email)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

app.run(debug = True , port = 3000)