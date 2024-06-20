from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()], render_kw={"type": "email"},)
    senha = PasswordField('Senha', validators=[DataRequired()])
    nivel_id = SelectField('Nivel', coerce=int, validators=[DataRequired()])