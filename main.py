from datetime import datetime
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
	# import ipdb; ipdb.set_trace()
	if request.method == 'POST':
		
		""" Add entry to the database"""
		name = request.form.get('name')
		email = request.form.get('email')
		phone = request.form.get('phone')
		message = request.form.get('message')
	
		""" sno, name,email,phone_num, date"""

		print(name, email, phone, message)
	return render_template('contact.html')

@app.route("/post")
def post():
	return render_template('post.html')


if __name__=='__main__':
	app.run(debug=True)