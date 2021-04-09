from flask import Flask, render_template ,request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/enchatmoves'

db = SQLAlchemy(app)



class Contacts(db.Model):
    srNo = db.Column(db.Integer ,primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Email = db.Column(db.String(30), nullable=False)
    Phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(90),nullable=False)
    time = db.Column(db.String(12), nullable=True)


@app.route("/", methods = ['GET','POST'])
def home():
    if(request.method=="POST"):
        '''adding entry to database '''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(Name=name,Email=email,Phone=phone,message=message,time= datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')





app.run(debug=True)