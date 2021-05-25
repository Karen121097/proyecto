
from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def url_principal():
	return render_template("template.html",nombre="Karen")

@app.route("/principal")
def principal():
	return render_template("template3.html")

@app.route("/pasa")
def pasa():
	return render_template("template2.html")

@app.route("/contacto")
def contacto():
	return render_template("template4.html")

if __name__ == '__main__':
	app.run(debug=True)