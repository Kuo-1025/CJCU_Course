from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length

class AddProductForm(FlaskForm):
    BookName = StringField('書名', validators=[DataRequired(), Length(min=1, max=100)])
    category = StringField('商品分類：', validators=[DataRequired()])
    author = StringField('作者', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('商品描述', validators=[Length(max=500)])
    price = DecimalField('價格', validators=[DataRequired()])
    quantity = DecimalField('商品數量', validators=[DataRequired()])
    submit = SubmitField('上架')