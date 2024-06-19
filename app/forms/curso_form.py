from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired
class CursoForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])
     escola_id = SelectField('Escola', coerce=int, validators=[DataRequired()])