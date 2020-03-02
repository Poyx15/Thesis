
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float
from datetime import datetime
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="BahaPhilippines2",
    password="thesis2020",
    hostname="BahaPhilippines2020.mysql.pythonanywhere-services.com",
    databasename="BahaPhilippines2$BahaDB",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Announcement(db.Model):

    __tablename__ = "Announcements"

    id = db.Column(db.Integer, primary_key=True)
    actualheight = db.Column(db.Float())
    level = db.Column(db.Integer)
    message = db.Column(db.String(250))
    posted = db.Column(db.DateTime, default=datetime.now)


@app.route("/")
def index():
    return render_template("home_page.html")

@app.route('/announcements', methods=["GET", "POSTS"])
def announcement():
    return render_template("announcement_page.html", Announcements=reversed(Announcement.query.all()))


@app.route('/posts', methods=['POST'])
def posts():
    req_data = request.get_json()

    ActualHeight = req_data['ActualHeight']
    Level = req_data['Level']
    Message = req_data['Message']

    data = Announcement(actualheight=ActualHeight, level=Level, message=Message)
    db.session.add(data)
    db.session.commit()

    return '''The Actual Height is {}.
    The Level is {}.
    The message: {}.
    Time Posted: {}.
    '''.format(ActualHeight, Level, Message, datetime.now)





