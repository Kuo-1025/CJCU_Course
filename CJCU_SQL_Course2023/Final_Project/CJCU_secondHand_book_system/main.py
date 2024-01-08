from Department_category import Departments
from flask import Flask, render_template, redirect, url_for, flash, jsonify, session, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from Login import LoginForm
from Registeration import RegisterationForm
from addProducts import AddProductForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

db = SQLAlchemy(app)

class UserAccount(db.Model):
    U_id = db.Column(db.Integer, primary_key=True)
    U_name = db.Column(db.String(50), unique=True, nullable=False)
    U_gender = db.Column(db.String(5), nullable=True)
    U_p4sswd = db.Column(db.String(255), nullable=False)

class Product(db.Model):
    B_id = db.Column(db.Integer, primary_key=True)
    B_name = db.Column(db.String(100), nullable=False)
    B_category = db.Column(db.String(20), nullable=False)
    B_author = db.Column(db.String(50), nullable=False)
    B_description = db.Column(db.String(500))
    B_price = db.Column(db.Integer, nullable=False)
    B_quantity = db.Column(db.Integer, nullable=False)
    S_id = db.Column(db.Integer, db.ForeignKey('user_account.U_id'), nullable=False)
    
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    B_id = db.Column(db.Integer, db.ForeignKey('product.B_id'), nullable=False)
    B_quantity = db.Column(db.Integer, nullable=False)
    U_id = db.Column(db.Integer, db.ForeignKey('user_account.U_id'), nullable=False)

@app.route('/')
def index():
    allProducts = Product.query.all()
    
    return render_template('main.html', products=allProducts, Departments=Departments[1:])

@app.route('/category/<category>')
def category(category):
    products = Product.query.filter_by(B_category=category).all()
    
    return render_template('showCategoryProduct.html', category=category, products=products, Departments=Departments)

@app.route('/search', methods=['GET'])
def searchProducts():
    keywordInp = request.args.get('keyword')

    searchResult = Product.query.filter(or_(Product.B_name.ilike(f"%{keywordInp}%"))).all()
    
    return jsonify(productsList=[{'B_id':product.B_id, 'B_name':product.B_name, 'B_author':product.B_author, 'B_price':product.B_price} for product in searchResult])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    
    if form.validate_on_submit():
        username = form.UserName.data
        
        #selected_gender = request.form.get('gender')
        userpasswd = generate_password_hash(form.UserP4sswd.data, method='sha512')
            
        new_User = UserAccount(U_name=username, U_p4sswd=userpasswd)
        
        try:
            db.session.add(new_User)
            db.session.commit()
            
            return redirect(url_for('index'))
        except Exception as e:
            print("registeration failed")
            db.session.rollback()
    
    return render_template('register.html', form=form)

@app.route('/check_username/<username>', methods=['GET'])
def check_username(username):
    existing_user = UserAccount.query.filter_by(U_name=username).first()
    
    if existing_user:
        print('該用戶名已被使用')
        return jsonify({'message':'該用戶名已被使用'}), 409
    else:
        print('該用戶名尚未被使用')
        return jsonify({'message':'該用戶名尚未被使用'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.UserName.data
        userpasswd = form.UserP4sswd.data
        
        cur_user = UserAccount.query.filter_by(U_name=username).first()

        if cur_user and check_password_hash(cur_user.U_p4sswd, userpasswd):
            flash('登入成功！', 'success')
            
            session['username'] = username
            
            return redirect(url_for('index'))
        else:
            error_message = '使用者名稱或密碼錯誤'
            
            return render_template('login.html', form=form, error_message=error_message)
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    
    return redirect(url_for('index'))

@app.route('/user_profile/<username>')
def user_profile(username):
    user = UserAccount.query.filter_by(U_name=username).first()
    
    userProducts = Product.query.filter_by(S_id=user.U_id).all()
    
    return render_template('userProfile.html', user=user, userProducts=userProducts, Departments=Departments[1:])

@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    
    if 'username' in session:
        form = AddProductForm()
        
        if form.validate_on_submit():
            cur_user = UserAccount.query.filter_by(U_name=session['username']).first()
            
            selected_category = request.form.get('category')
            
            new_product = Product(
                B_name=form.BookName.data,
                B_category=selected_category,
                B_author=form.author.data,
                B_description=form.description.data,
                B_price=form.price.data,
                B_quantity=form.quantity.data,
                S_id=cur_user.U_id
            )
        
            db.session.add(new_product)
            db.session.commit()

            return redirect(url_for('index'))
        
    return render_template('addProducts.html', form=form, Departments=Departments)

@app.route('/show_product_detail/<int:P_id>')
def show_product_detail(P_id):
    product = Product.query.get_or_404(P_id)
    
    return render_template('showProductDetail.html', product=product)

@app.route('/add_to_cart/<int:P_id>', methods=['POST'])
def add_to_cart(P_id):
    product = Product.query.get_or_404(P_id)
    
    cur_user = UserAccount.query.filter_by(U_name=session['username']).first()
    
    cart_item = CartItem.query.filter_by(B_id=product.B_id, U_id=cur_user.U_id).first()
    if cart_item:
        cart_item.B_quantity += 1
        
    else:
        new_item = CartItem(B_id=P_id, B_quantity=1, U_id=cur_user.U_id)
        
        db.session.add(new_item)
        
    db.session.commit()
    
    return redirect(url_for('show_product_detail', P_id=P_id))

@app.route('/show_cart')
def show_cart():
    cur_user = UserAccount.query.filter_by(U_name=session['username']).first()
    cart_items = CartItem.query.filter_by(U_id=cur_user.U_id).all()
    
    cartList = []
    for item in cart_items:
        cur_Product = Product.query.get_or_404(item.B_id)
        
        cartList.append([item.id, cur_Product.B_id, cur_Product.B_name, cur_Product.B_price, item.B_quantity])
    
    return render_template('showCart.html', cart_items=cartList)

@app.route('/check_quantity/<int:p_id>/<int:newQuantity>', methods=['GET'])
def check_quantity(p_id, newQuantity):
    print('check')
    cur_product = Product.query.get_or_404(p_id)
    print(1)
    
    if 1 <= newQuantity <= cur_product.B_quantity:
        print('valid')
        return jsonify({'success':True, 'message':'Quantity is in range'})
    else:
        return jsonify({'success':False, 'message':f'Quantity must in 1 ~ {cur_product.B_quantity}'})

@app.route('/update_quantity/<int:p_id>/<int:newQuantity>', methods=['POST'])
def update_quantity(p_id, newQuantity):
    print('update')
    print(f'newQuantity is {newQuantity}')
    cur_user = UserAccount.query.filter_by(U_name=session['username']).first()
    cur_item = CartItem.query.filter_by(U_id=cur_user.U_id, B_id=p_id).first()
    print(f'{cur_item.U_id}->{cur_item.B_id} quantity before update is {cur_item.B_quantity}')
    cur_item.B_quantity = newQuantity
    print(f'{cur_item.U_id}->{cur_item.B_id} quantity after update is {cur_item.B_quantity}')
        
    db.session.commit()
    
    return jsonify({'success':True, 'message':'Quantity updated seccessfully'})

@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    
    db.session.delete(cart_item)
    db.session.commit()
    
    return redirect(url_for('show_cart'))
            
if __name__ == "__main__":
    app.run(debug=True)