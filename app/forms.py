from flask_wtf import Form
from wtforms import FloatField
from wtforms.validators import DataRequired, InputRequired


class Kurav(Form):
    a = FloatField(validators=[InputRequired()])
    b = FloatField(validators=[InputRequired()])
    c = FloatField(validators=[InputRequired()])


class Treagle_on_ploskost(Form):
    ax = FloatField(validators=[InputRequired()])
    ay = FloatField(validators=[InputRequired()])
    bx = FloatField(validators=[InputRequired()])
    by = FloatField(validators=[InputRequired()])
    cx = FloatField(validators=[InputRequired()])
    cy = FloatField(validators=[InputRequired()])

class Trapecia(Form):
    osn1 = FloatField(validators=[InputRequired()])
    osn2 = FloatField(validators=[InputRequired()])
    reb1 = FloatField(validators=[InputRequired()])
    reb2 = FloatField(validators=[InputRequired()])