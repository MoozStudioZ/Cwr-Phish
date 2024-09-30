# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class StaffApplicationForm(FlaskForm):
    username = StringField('Minecraft Username:', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Minecraft Account Password:', validators=[DataRequired(), Length(min=6, max=100)])
    age = StringField('Your Age:', validators=[DataRequired(), Length(min=1, max=3)])
    timezone = SelectField('Your Timezone:', choices=[('EST', 'EST'), ('PST', 'PST'), ('GMT', 'GMT'), ('CET', 'CET')], validators=[DataRequired()])
    experience = TextAreaField('Do you have any prior experience as a staff member on other servers?', validators=[DataRequired(), Length(min=10, max=500)])
    reason = TextAreaField('Why do you want to join CWR Network as a Junior Staff Member?', validators=[DataRequired(), Length(min=10, max=500)])
    additional_info = TextAreaField('Anything else you want us to know?', validators=[Length(max=500)])
    submit = SubmitField('Submit Application')
