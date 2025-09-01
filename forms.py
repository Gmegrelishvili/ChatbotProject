from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField, DateField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, length, EqualTo

class RegisterForm(FlaskForm):
     username = StringField("Username", validators=[DataRequired(), length(min=4, max=16)])
     password = PasswordField("Password", validators=[DataRequired(), length(min=8, max=16)])
     repeat_password = PasswordField("Repeat password", validators=[EqualTo("password", message="პაროლები არ ემთხვევა")])
     birthday = DateField("Date of birth")
     country = SelectField("Select a country", choices=["Select a country", "Georgia", "Germany", "France"])
     gender = RadioField("Please indicate gender.", choices=["Male", "Female"])

     submit = SubmitField("REGISTRATION")


class MessageForm(FlaskForm):
     message = TextAreaField("Enter a text")
     submit = SubmitField("Send")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), length(min=3, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), length(min=6)])
    submit = SubmitField("Log In")