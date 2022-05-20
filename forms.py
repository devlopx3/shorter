from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from models import url_data


class AddLink(FlaskForm):
    url = StringField('url',
                           validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Create Short')  



    def validate_original_url(self, url):
    	url_exist = url_data.query.filter_by(original_url=url.data).first()
    	if url_exist:
    		raise ValidationError('That email is taken. Please choose a different one.')




