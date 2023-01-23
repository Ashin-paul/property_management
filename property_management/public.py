from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('index.html')

@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		pwd=request.form['pa']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		res=select(q)
		if res:
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))

			elif res[0]['usertype']=="user":
				q1="select * from user where login_id='%s'"%(res[0]['login_id'])
				res1=select(q1)
				session['userid']=res1[0]['user_id']
				flash("login successfully")
				return redirect(url_for('user.userhome'))

		else:
			flash("invaild username and password")
	return render_template('login.html')



@public.route('/userregister',methods=['get','post'])
def userregister():
	if "register" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		pl=request.form['place']
		pin=request.form['pin']
		h=request.form['h']
		ph=request.form['phone']
		em=request.form['email']
		uname=request.form['uname']
		pwd=request.form['pwd']

		ql="insert into login values(null,'%s','%s','user')"%(uname,pwd)
		rl=insert(ql)
		qs="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(rl,f,l,h,pl,pin,ph,em)
		insert(qs)
		flash("register successfully")
		return redirect(url_for('public.userregister'))
		
	return render_template('userregister.html')