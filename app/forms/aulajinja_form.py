from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired,NumberRange
class AulaJinjaForm(FlaskForm):
     x = IntegerField("x",validators=[DataRequired()],default=12)
    