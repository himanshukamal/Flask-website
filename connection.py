import sqlite3

conn = sqlite3.connect('blog_contact.db')
print("Opened database successfully");

# conn.execute('CREATE TABLE entries (name TEXT, email TEXT, phone TEXT, message TEXT)')
# print("Table: entries created successfully");

conn.execute('CREATE TABLE articles (title TEXT, content TEXT)')
print("Table: articles created successfully");

conn.close()