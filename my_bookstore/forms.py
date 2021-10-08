from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField 
from wtforms.validators import DataRequired,Email

class AddForm(FlaskForm):

    name = StringField('Name of Book:')
    submit = SubmitField('Add Book')

class DelForm(FlaskForm):

    isbn = IntegerField('ISBN Number of Book to Remove:')
    submit = SubmitField('Remove Book')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
