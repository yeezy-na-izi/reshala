from flask_wtf import Form
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired


class Kurav(Form):
    a = FloatField(validators=[DataRequired()])
    b = FloatField(validators=[DataRequired()])
    c = FloatField(validators=[DataRequired()])


class Treagle_on_ploskost(Form):
    ax = FloatField(validators=[DataRequired()])
    ay = FloatField(validators=[DataRequired()])
    bx = FloatField(validators=[DataRequired()])
    by = FloatField(validators=[DataRequired()])
    cx = FloatField(validators=[DataRequired()])
    cy = FloatField(validators=[DataRequired()])

class Trapecia(Form):
    osn1 = FloatField(validators=[DataRequired()])
    osn2 = FloatField(validators=[DataRequired()])
    reb1 = FloatField(validators=[DataRequired()])
    reb2 = FloatField(validators=[DataRequired()])