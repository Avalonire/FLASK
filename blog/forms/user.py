from wtforms import Form, StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm


class UserRegisterForm(FlaskForm):
    username = StringField('Username')
    email = StringField('email', [
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Field must be equal to password!')
    ])
    confirm_password = PasswordField('Confirm password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Register')

