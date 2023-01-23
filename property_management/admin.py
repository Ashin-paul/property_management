from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('adminhome')
def adminhome():
	return render_template('adminhome.html')

@admin.route('adminviewuser')
def adminviewuser():
	data={}
	q="select * from user"
	r=select(q)
	data['users']=r
	return render_template('adminviewuser.html',data=data)

@admin.route('/adminviewcomplaint',methods=['get','post'])
def adminviewcomplaint():
	data={}
	q="SELECT * FROM complaint INNER JOIN user using (user_id)"
	r=select(q)
	data['complaints']=r
	return render_template('adminviewcomplaint.html',data=data)

@admin.route('/adminsendreply',methods=['get','post'])
def adminsendreply():
	if "send" in request.form:
		r=request.form['r']
		cid=request.args['cid']
		q="update complaint set reply='%s' where complaint_id='%s'"%(r,cid)
		update(q)
		flash("send successfully")
		return redirect(url_for('admin.adminviewcomplaint'))

	return render_template('adminsendreply.html')


@admin.route('/adminmanagecategory',methods=['get','post'])
def adminmanagecategory():
	data={}
	if "add" in request.form:
		categories=request.form['cate']
		
		q="insert into category values(null,'%s')"%(categories)
		insert(q)
		flash("added successfully")
		return redirect(url_for("admin.adminmanagecategory"))
	
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
		
	if "update" in request.form:
		categories=request.form['cate']
		
		q="update category set category='%s' where category_id='%s'"%(categories,cid)
		insert(q)
		flash("update successfully")

		return redirect(url_for("admin.adminmanagecategory"))
	if action=="update":
		q="select * from category where  category_id='%s'" %(cid)
		res=select(q)
		data['updatecategorys']=res
	if action=="delete":
		q="delete from  category  where category_id='%s'" %(cid)
		delete(q)
		flash("delete successfully")
		return redirect(url_for("admin.adminmanagecategory"))
	
	q="select * from category"
	res=select(q)
	data['categorys']=res
	return render_template('adminmanagecategory.html',data=data)
@admin.route('/adminmanageproperty',methods=['get','post'])
def adminmanageproperty():
	data={}
	q="select * from  property inner join user using(user_id) inner join category using(category_id)"
	r=select(q)
	data['view']=r
	q="select * from user  "
	r=select(q)
	data['user']=r
	q="select * from category"
	r=select(q)
	data['cat']=r
	if "add" in request.form:
		u=request.form['u']
		c=request.form['c']
		p=request.form['p']
		a=request.form['a']
		d=request.form['d']
		qs="insert into property values(null,'%s','%s','%s','%s','%s',now(),'pending')"%(u,c,p,a,d)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanageproperty'))
	if "action" in request.args:
		action=request.args['action']
		property_id=request.args['property_id']
	else:
		action=None
	if "update" in request.form:
		u=request.form['u']
		c=request.form['c']
		p=request.form['p']
		a=request.form['a']
		d=request.form['d']
		q="update property set user_id='%s',category_id='%s',property_title='%s',amount='%s',description='%s',date_time=now() where property_id='%s'"%(u,c,p,a,d,property_id)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanageproperty'))
	if action=="update":
		q="select * from  property inner join user using(user_id) inner join category using(category_id) where property_id='%s'"%(property_id)
		r=select(q)
		data['updates']=r
	if action=="delete":
		q="delete from property where property_id='%s'"%(property_id)
		delete(q)
		flash("delete successfully")

		return redirect(url_for('admin.adminmanageproperty'))
 
	return render_template('adminmanageproperty.html',data=data)


