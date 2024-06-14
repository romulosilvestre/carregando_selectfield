from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class EscolaForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])
     telefone = StringField("telefone",validators=[DataRequired()])