# coding: utf8
from app import app
from flask import render_template, request, redirect, url_for, flash


@app.route('/')
def index( nom = None ):
   return render_template( 'index.html' )

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
