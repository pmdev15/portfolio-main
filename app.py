from flask import Flask,render_template,flash
from forms import ConatactForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone


#Create a flask instance
app = Flask(__name__)

#csrf token #hide when uploading to github
app.config['SECRET_KEY'] = "my super secret key"

#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# #initilize the database
db = SQLAlchemy(app)

# Message Database
class Message(db.Model):
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False,primary_key = True, unique = True)  
    subject = db.Column(db.String(30), nullable = False, unique = True)
    message = db.Column(db.Text(), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    #Create a string
    def __repr__(self):
        return '<Name %r>' % self.name

# # Blog Database
# class Blog(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(100), nullable = False)
#     date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))
#     desc = db.Column(db.Text, nullable = False)
#     content = db.Colunm(db.Text, nullable = False)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/blog')
def blog(name):
    return render_template("blog.html",user_name=name)

# Projects List
@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    form = ConatactForm()
    if form.validate_on_submit():
        msg = Message(name=form.name.data,email=form.email.data,subject=form.subject.data,message=form.message.data)
        db.session.add(msg)
        db.session.commit()
        flash("Message Send Succesfully!!")
        form.name.data = ''
        form.email.data = ''
        form.subject.data = ''
        form.message.data = ''
    return render_template("contact.html", form=form)

@app.route('/admin')
def admin():
    return render_template("admin.html")

#Custom Error Page

#invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500
