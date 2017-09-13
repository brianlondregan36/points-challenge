from points import app
from flask import Flask, render_template, request, redirect, url_for


@app.route('/')
def index():
	'''code goes here'''
	data = ""
	return render_template("index.html", data)

