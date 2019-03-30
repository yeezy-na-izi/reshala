from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class Kurav(Form):
    a = StringField(validators=[DataRequired()])
    b = StringField(validators=[DataRequired()])
    c = StringField(validators=[DataRequired()])


class Treagle_on_ploskost(Form):
    ax = StringField(validators=[DataRequired()])
    ay = StringField(validators=[DataRequired()])
    bx = StringField(validators=[DataRequired()])
    by = StringField(validators=[DataRequired()])
    cx = StringField(validators=[DataRequired()])
    cy = StringField(validators=[DataRequired()])

class Trapecia(Form):
    osn1 = StringField(validators=[DataRequired()])
    osn2 = StringField(validators=[DataRequired()])
    reb1 = StringField(validators=[DataRequired()])
    reb2 = StringField(validators=[DataRequired()])