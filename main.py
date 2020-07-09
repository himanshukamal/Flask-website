import sqlite3 as sql
from datetime import datetime
from flask import Flask, render_template, request

# conn = sql.connect('database.db')
# print ["Opened database successfully"];
# conn.execute('CREATE TABLE blog_contact (name TEXT, email TEXT, phone TEXT, message TEXT)')
# print ["Table created successfully"]
# conn.close()

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
		try:
			name = request.form.get('name')
			email = request.form.get('email')
			phone = request.form.get('phone')
			message = request.form.get('message')
		
			with sql.connect("blog_contact.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO entries (name,email,phone,message)VALUES (?,?,?,?)",(name,email,phone,message) )
				# """ sno, name,email,phone_num, date"""
				con.commit()
				msg = "Record successfully added"

		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html",msg = msg)
			con.close()
	return render_template('contact.html')

@app.route("/post")
def post():
	return render_template('post.html')


@app.route("/write", methods=['GET', 'POST'])
def write():
	if request.method == "POST":

		try:
			title = request.form.get('title')
			content = request.form.get('content')
		
			with sql.connect("blog_contact.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO articles (title,content)VALUES (?,?)",(title,content) )
				# """ sno, name,email,phone_num, date"""
				con.commit()
				msg = "Record successfully added"

		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html",msg = msg)
			con.close()

	return render_template('write.html')



if __name__=='__main__':
	app.run(debug=True)