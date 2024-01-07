from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    UserName = StringField('使用者名稱', validators=[DataRequired(), Length(min=4, max=20)])
    UserP4sswd = PasswordField('密碼', validators=[DataRequired(), Length(min=6, max=20)])
    Submit = SubmitField('登入')