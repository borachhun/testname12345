from flask import Flask, redirect, render_template, request

import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

conn = sqlite3.connect("database.db")
db = conn.cursor()

@app.route("/")
def index():
	db.execute("SELECT * FROM names")
	rows = db.fetchall()
	return render_template("index.html", rows=rows)

@app.route("/add", methods=["GET", "POST"])
def add():
	if request.method == "GET":
		return render_template("add.html")
	else:
		name = request.form.get("name")
		db.execute("INSERT INTO names (name) VALUES (?)", name)
		conn.commit()
		return render_template("name.html", name=name)
