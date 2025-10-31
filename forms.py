from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

#Conatct Class
class ConatactForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired(),Email()])
    subject = StringField("What's this About",validators=[DataRequired(),Length(max=30)])
    message = StringField("Tell Your Mind!!!",validators=[DataRequired()])
    submit = SubmitField("Send Message")

# Blog Class
class BlogForm(FlaskForm):
    title = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    subject = StringField("What's this About",validators=[DataRequired(),Length(max=30)])
    message = StringField("Tell Your Mind!!!",validators=[DataRequired()])
    submit = SubmitField("Send Message")

