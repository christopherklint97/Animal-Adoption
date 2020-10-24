from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import AnyOf, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet name")
    species = StringField('Species', [AnyOf(
        ['cat', 'dog', 'porcupine'], message='The species must be a cat, dog, or porcupine')])
    photo_url = StringField('Photo URL', [
        URL(require_tld=False, message='The photo must be a url'),
        Optional()
    ])
    age = IntegerField('Age', [NumberRange(
        min=0, max=30, message='The age must be between 0 and 30')])
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', [
        URL(require_tld=False, message='The photo must be a url'),
        Optional()
    ])
    notes = StringField('Notes')
    available = BooleanField('Available')
