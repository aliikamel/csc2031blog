from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, NoneOf, Length, ValidationError
from users.validation import*


class RegisterForm(FlaskForm):

    username = StringField(validators=[DataRequired(), Email(), character_check])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15), character_check, validate_number, validate_lowercase])
    confirm_password = PasswordField(validators=[DataRequired(), validate_password])
    submit = SubmitField()









