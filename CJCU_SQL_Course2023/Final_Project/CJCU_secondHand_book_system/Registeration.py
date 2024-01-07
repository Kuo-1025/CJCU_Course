from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterationForm(FlaskForm):
    UserName = StringField('使用者名稱', validators=[DataRequired(), Length(min=4, max=20)])
    UserP4sswd = PasswordField('密碼', validators=[DataRequired(), Length(min=6, max=20), EqualTo('checkP4sswd', message="需與上述密碼一致")])
    checkP4sswd = PasswordField('確認密碼', validators=[DataRequired()])
    Submit = SubmitField('註冊')