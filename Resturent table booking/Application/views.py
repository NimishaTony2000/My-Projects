from flask import Blueprint, render_template, request, flash, jsonify,redirect
from flask_login import login_required, current_user,login_user
from . import db
import datetime
from .models import Registraion,Login
from werkzeug.security import generate_password_hash,check_password_hash
views = Blueprint('views', __name__)

# @views.route('/',methods=['GET','POST'])                   
# def home():      
#     if request.method=='POST':
#         vno=request.form.get('vnumber')
#         phone=request.form.get('number')
#         car_obj=car(carNumber=vno,Ph=phone)       
#         db.session.add(car_obj)
#         db.session.commit()   
#         return render_template('price.html')                     
#     return render_template('index.html')



@views.route('/',methods=['GET','POST'])                   
def home(): 
    return render_template('home.html')

@views.route('/index',methods=['GET','POST'])                   
def index(): 
    return render_template('index.html')

@views.route('/user_sign',methods=['GET','POST'])                   
def user_sign(): 
    if request.method=='POST':
        username=request.form.get('email')
        password=request.form.get('password')
        log=Login.query.filter_by(email=username).first()
        print(log)
        if log:
            if check_password_hash(log.password,password):
                if log.user_type=='c':
                    login_user(log,remember=True)
                    return render_template('index.html')
                if log.user_type=='r':
                    login_user(log,remember=True)
                    return render_template('user_sign.html')
            return render_template('user_sign.html')
        return render_template('user_sign.html')
    return render_template('user_sign.html')
@login_required
@views.route('/payment',methods=['GET','POST'])                   
def payment(): 
    return render_template('payment.html')

@views.route('/user_reg',methods=['GET','POST'])                   
def user_reg(): 
    if request.method=='POST':
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        address=request.form.get('Address')
        password=request.form.get("password1")
        passw=generate_password_hash(password,method='sha256')
        
        new_user=Registraion(name=name,phone=phone,email=email,address=address,password=passw)
        db.session.add(new_user)
        db.session.commit()
        log=Login(email=email,password=passw,user_type='c')
        db.session.add(log)
        db.session.commit()
        return redirect('/')
    return render_template('user_reg.html')

@views.route('/admin_page',methods=['GET','POST'])                   
def admin_page(): 
    return render_template('admin_page.html')

@views.route('/admin_resv',methods=['GET','POST'])                   
def admin_resv(): 
    return render_template('admin_resv.html')
@login_required
@views.route('/book',methods=['GET','POST'])                   
def book(): 
    return render_template('book.html')

@views.route('/Edit_details',methods=['GET','POST'])                   
def Edit_details(): 
    return render_template('Edit_details.html')

#css load avathe thazhekk

@views.route('/rest_reg',methods=['GET','POST'])                   
def rest_reg(): 
    return render_template('rest_reg.html')

@views.route('/tables',methods=['GET','POST'])                   
def tables(): 
    return render_template('tables.html')

@views.route('/rest_home',methods=['GET','POST'])                   
def rest_home(): 
    return render_template('rest_home.html')

@views.route('/user_details',methods=['GET','POST'])                   
def Users_Details(): 
    return render_template('user_details.html')

@views.route('/Resturents_details',methods=['GET','POST'])                   
def Resturents_details(): 
    return render_template('Resturents_details.html')

@views.route('/Reservations',methods=['GET','POST'])                   
def Reservations(): 
    return render_template('Reservations.html')















