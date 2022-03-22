from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class NewPropertyForm(FlaskForm):
    title = StringField("Property Title:", validators=[DataRequired()])
    description = TextAreaField("Description:", validators=[DataRequired()])
    rooms = StringField("No. of Rooms:", validators=[DataRequired()])
    bathrooms = StringField("No. of Bathrooms:", validators=[DataRequired()])
    price = StringField("Price:", validators=[DataRequired()])
    propertytype = SelectField('Property Type:', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField("Location:", validators=[DataRequired()])
    photo = FileField("Photo:", validators=[FileRequired(), FileAllowed(['jpg', 'png'],'Image Files Only!')])
