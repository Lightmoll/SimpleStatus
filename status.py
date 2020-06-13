from utils import html_sanatize
import passwlib

import os
import math
import random
import string
import datetime

from flask import Flask, request, send_from_directory
from flask import render_template, redirect, make_response
app = Flask(__name__)

data_path = os.getcwd()
session_str_path = os.path.join(data_path, "data/session_str.txt")
db_path = os.path.join(data_path, "data/status.db")
e_mail_list_path = os.path.join(data_path,  "data/e_mail.db")

debug = False

@app.route("/logout")
def logout():
	with open(session_str_path, "r", encoding="utf-8") as file:
		curr_session = file.read()
	if request.cookies.get("session") == curr_session and request.method == "GET":
		curr_session = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(200))
		with open(session_str_path, "w", encoding="utf-8") as file:
			file.write(curr_session)
	return redirect("/", 302)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		data = []
		lines = []

		with open(db_path, "r", encoding ="utf-8") as file:
			lines = file.readlines()
		for i in range(len(lines),0,-4):
			data.append({
				"title": lines[i-4][:-1],
				"location": lines[i-3][:-1],
				"body":lines[i-2][:-1],
				"time":lines[i-1][:-1]})
		with open(session_str_path, "r", encoding="utf-8") as file:
			curr_session = file.read();
		#if request.cookies.get("session") == curr_session and request.method == "GET":
		#	return render_template("admin_index_template.html", data=data)
		#else:
		#	return render_template("index_template.html", data=data)
		return render_template("index_template.html", data=data)
	else:
		with open(e_mail_list_path, "a") as file:
			file.write(request.form["email"])
			file.write("\n")

		return redirect("#email_added",302)

@app.route("/push", methods=["GET", "POST"])
def push():
	with open(session_str_path, "r", encoding="utf-8") as file:
		curr_session = file.read()
	if request.cookies.get("session") == curr_session and request.method == "GET":
		return send_from_directory("html/", "push.html")

	elif request.method == "GET":
		resp = make_response(send_from_directory("html/", "login.html"))
		resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
		resp.headers["Pragma"] = "no-cache"
		resp.headers["Expires"] = "0"
		return resp
	else:
		try:
			input_password = request.form["password"]

			if passwlib.verify_password(input_password):
				curr_session = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(120))
				with open(session_str_path, "w", encoding="utf-8") as file:
					file.write(curr_session)

				resp = make_response(send_from_directory("html/", "push.html"))
				expire_date = datetime.datetime.now() + datetime.timedelta(days=90)

				if debug:
					resp.set_cookie("session", curr_session, expires=expire_date)
				else:
					resp.set_cookie("session", curr_session, secure=True, httponly=True, samesite="Strict", expires=expire_date)

				resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
				resp.headers["Pragma"] = "no-cache"
				resp.headers["Expires"] = "0"

				return resp
			else:
				return redirect("#wrong_password", 302)

		except Exception:
			if curr_session == request.cookies.get("session"):
				with open(db_path, "a", encoding="utf-8") as file:
						file.write(request.form["title"] + "\n")
						file.write(request.form["position"] + "\n")
						file.write(html_sanatize(request.form["body"]) + "\n")
						tm = str(datetime.datetime.utcnow())+"Z"
						file.write(tm + "\n")
				return send_from_directory("html/", "push.html")
	return send_from_directory("html/", "login.html")

if __name__ == "__main__":
	debug = True
	app.run(port=8500, debug=True)
