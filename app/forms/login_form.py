from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired()], render_kw={"type": "email"},)
    senha = PasswordField('Senha', validators=[DataRequired()])
