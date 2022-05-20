from flask import render_template, url_for, flash, redirect, request,Flask
from flask_sqlalchemy import SQLAlchemy
from flask import make_response
import string
from random import choices
import requests
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

######################################
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '6aa36c97f1e371272ba6e8003e493aba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#####################################



class AddLink(FlaskForm):
    url = StringField('url',
                           validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Create Short')  



    def validate_original_url(self, url):
    	url_exist = url_data.query.filter_by(original_url=url.data).first()
    	if url_exist:
    		raise ValidationError('That email is taken. Please choose a different one.')




class url_data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(200), unique=True, nullable=False)
	short_url = db.Column(db.String(6), unique=True)
	visits = db.Column(db.Integer, default=0)




	def __repr__(self):
		return f"urls_data'{self.original_url}','{self.short_url}',{self.visits}"

class info(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userIP = db.Column(db.String(50), nullable=False)
	country = db.Column(db.String(50), nullable=False)
	city = db.Column(db.String(50), nullable=False)
	for_short = db.Column(db.String(50), nullable=False)
	time = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return f"info'{self.userIP}','{self.country}',{self.city},'{self.for_short}','{self.time}'"

@app.route('/<short_url>')
def redirect_to_url(short_url):
    link = url_data.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    

    db.session.commit()    
    r = make_response(redirect(link.original_url, code=301))
    r.headers.set('alt-svc', "clear")
    r.headers.set('cache-control', "private, max-age=90")
    r.headers.set('content-security-policy', "referrer always;")
    r.headers.set('referrer-policy', "unsafe-url")
    r.headers.set('server', "nginx")
    r.headers.set('via', "1.1 google")
    


    return  r


@app.route('/')
def index():
	return redirect(url_for('add_link'))
	

		

	return render_template('add_link.html',form=form)


@app.route('/add_link', methods=['POST','GET'])
def add_link():
	form = AddLink()
	db.create_all()	
	if form.validate_on_submit():
		url_exist = url_data.query.filter_by(original_url=form.url.data).first()
		if url_exist:
			flash('Created UnSuccesfull Already Shorted','danger')
		else:
			characters = string.digits + string.ascii_letters
			short_url = ''.join(choices(characters, k=6))
			url_1 = url_data(original_url=form.url.data,short_url=short_url)
			
			db.session.add(url_1)
			db.session.commit()
			
			flash(f'Created Succesfull', 'success')
			return redirect(url_for('index'))



		

	return render_template('add_link.html',form=form,db=db)

@app.route('/views')
def views():
    links = url_data.query.all()
    
    return render_template('views.html', links=links,db=db)

@app.route('/delete') 
def delete():
	db.drop_all()
	flash(f'All Date Deleted Succesfull', 'danger')
	return redirect(url_for('index'))




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=5000)
