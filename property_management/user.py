from flask import *
from database import *
import uuid

user=Blueprint('user',__name__)

@user.route('userhome')
def userhome():
	return render_template('userhome.html')

@user.route('/userupdateprofile',methods=['get','post'])
def userupdateprofile():
	data={}
	sid=session['userid']
	q="select * from  user where user_id='%s'"%(sid)
	r=select(q)
	data['updates']=r
	
	if "update" in request.form:
		fna=request.form['f']
		lna=request.form['l']
		h=request.form['h']
		pla=request.form['pl']
		pin=request.form['pin']
		pho=request.form['ph']
		em=request.form['e']
		q="update user set firstname='%s',lastname='%s',housename='%s',place='%s',pincode='%s',phone='%s',email='%s' where user_id='%s'"%(fna,lna,h,pla,pin,pho,em,sid)
		print(q)
		r=update(q)
		flash(" profile updated successfully")
		return redirect(url_for('user.userupdateprofile'))
	return render_template('userupdateprofile.html',data=data)


@user.route('/usersendcomplaint',methods=['get','post'])
def usersendcomplaint():
	data={}
	q="select * from complaint"
	r=select(q)
	data['comp']=r
	if "send" in request.form:
		complaint=request.form['com']
		sid=session['userid']
		q="insert into complaint values(null,'%s','%s','reply-pending',now())"%(sid,complaint)
		insert(q)
		return redirect(url_for('user.usersendcomplaint'))
	return render_template('usersendcomplaint.html',data=data)




@user.route('userviewrequest',methods=['get','post'])
def userviewrequest():
	data={}
	userid=session['userid']
	q="SELECT *,request.user_id as ruserid FROM request INNER JOIN USER USING(user_id) INNER JOIN property USING(property_id) WHERE request.user_id<>'%s'"%(userid)
	r=select(q)
	data['view']=r
	return render_template('userviewrequest.html',data=data)


@user.route('useruploadnewproperty',methods=['get','post'])
def useruploadnewproperty():
	data={}
	userid=session['userid']
	if "upload" in request.form:
		i=request.files['i']
		pro=request.form['pro']
		path="static/assets/img"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into property_images values(null,'%s','%s')"%(pro,path)
		insert(q)
		flash('upload successfully')
		return redirect(url_for('user.useruploadnewproperty'))
	q="SELECT * FROM property inner join property_images using (property_id) "
	r=select(q)
	data['users']=r
	q="SELECT * FROM property"
	r=select(q)
	data['view']=r
	return render_template('useruploadnewproperty.html',data=data)

@user.route('userviewproperty',methods=['get','post'])
def userviewproperty():
	data={}
	userid=session['userid']
	q="SELECT * FROM category"
	r=select(q)
	data['cat']=r
	q="select * from  property inner join user using(user_id) inner join category using(category_id)"
	r=select(q)
	data['view']=r
	if "search" in request.form:
		sn=request.form['sname']
		q="select * from  property inner join user using(user_id) inner join category using(category_id) where category_id='%s'"%(sn)
		r=select(q)
		data['search']=r
		if r:
			data['search']=r
			print(data['search'])
		else:
			flash("NO MATCHED RESULTS FOUND")
	if "action" in request.args:
		action=request.args['action']
		# user_id=request.args['user_id']
		property_id=request.args['property_id']
		amount=request.args['amount']
	else:
		action=None
	if action=="requestproperty":
		q="insert into request values(null,'%s','%s','%s',now(),'pending')"%(userid,property_id,amount)
		insert(q)
		flash("request successfully")
		return redirect(url_for("user.userviewproperty"))
	
	return render_template('userviewproperty.html',data=data)


@user.route('userviewrequestedproperty',methods=['get','post'])
def userviewrequestedproperty():
	data={}
	# userid=session['userid']
	q="select * from request inner join user using(user_id) inner join property using(property_id) "
	r=select(q)
	data['view']=r
	return render_template('userviewrequestedproperty.html',data=data)

@user.route('usermakepayment',methods=['get','post'])
def usermakepayment():
	data={}
	request_id=request.args['request_id']
	total=request.args['total']
	data['total']=total
	if "payment" in request.form:
		q="insert into payment values(null,'%s','%s',curdate())"%(request_id,total)
		insert(q)
		flash('paid successfully')
		return redirect(url_for('user.userhome',request_id=request_id,total=total))
	
	return render_template('usermakepayment.html',data=data)


@user.route('userviewpayment',methods=['get','post'])
def userviewpayment():
	data={}
	# userid=session['userid']
	request_id=request.args['request_id']
	q="select * from payment where request_id='%s'"%(request_id)
	r=select(q)
	data['view']=r
	return render_template('userviewpayment.html',data=data)


@user.route('userchat',methods=['get','post'])
def userchat():
	data={}
	mid=session['userid']
	data['user']=mid
	oid=request.args['user_id']
	if "send" in request.form:
		msg=request.form['msg']
		oid=request.args['user_id']	
		q="insert into message values(null,'%s','%s','%s',now())"%(mid,oid,msg)
		insert(q)
		return redirect(url_for('user.userchat',user_id=oid))
	q="select * from message where (sender_id='%s'and receiver_id='%s') or (receiver_id='%s'and sender_id='%s')"%(mid,oid,mid,oid)
	r=select(q)
	data['view']=r
	return render_template('userchat.html',data=data)


@user.route('userchatusers',methods=['get','post'])
def userchatusers():
	data={}
	mid=session['userid']
	data['user']=mid
	oid=request.args['user_id']
	if "send" in request.form:
		msg=request.form['msg']
		oid=request.args['user_id']	
		q="insert into message values(null,'%s','%s','%s',now())"%(mid,oid,msg)
		insert(q)
		return redirect(url_for('user.userchatusers',user_id=oid))
	q="select * from message where (sender_id='%s'and receiver_id='%s') or (receiver_id='%s'and sender_id='%s')"%(mid,oid,mid,oid)
	r=select(q)
	print(q)
	data['view']=r
	return render_template('userchatusers.html',data=data)