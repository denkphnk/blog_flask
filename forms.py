from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class addNoteForm(FlaskForm):
    textarea = TextAreaField(validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField('Добавить')