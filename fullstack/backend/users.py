from flask import Flask, request
from flask_restx import Api, Resource, fields, Namespace, abort
from ...api.utils.utils import db
from http import HTTPStatus
from ...api.models.users import User
from ...api.models.data import Region, State, Lga, City, Area, load_dataset
from flask_caching import Cache
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash



auth = Namespace('User', description = 'Search related operations')


# signup route
@auth.route('/signup', methods = ['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form.get('username')
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		email = request.form.get('email')
		password = request.form.get('password')
		confirm_password = request.form.get('confirm_password')

		password_hash = generate_password_hash(password)
		email_exists = User.query.filter_by(email=email).first()
		if email_exists:
			flash('This mail already exists!', category='error')
		elif password != confirm_password:
			flash('Password does not match.', category='error')
		elif len(password) < 8:
			flash('Password is too short.', category='error')
		elif len(email) < 5:
			flash('Invalid email.', category='error')
		else:
			new_user = User(firstname=firstname, lastname=lastname, username = username, email = email, password_hash = password_hash)
			db.session.add(new_user)
			db.session.commit()
			flash('Your account has been created!')
			login_user(new_user, remember=True)

			return redirect(url_for('aven.index'))

	return render_template('register.html')



@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash(f"Good to have you back, {user.username}", category='success')
                login_user(user, remember=True)
                return redirect(url_for('aven.index'))
            else:
                flash("Incorrect password!", category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if 'authenticated' in session:
#         # User is already authenticated, redirect to dashboard or home page
#         return redirect('/dashboard')

#     if request.method == 'POST':
#         # Process login form data and authenticate the user
#         username = request.form['username']
#         password = request.form['password']
#         # Perform user authentication logic here

#         # Set session variable to indicate user is authenticated
#         session['authenticated'] = True

#         # Redirect to a different page after successful login
#         return redirect('/dashboard')

#     # Render the login or register template based on authentication status
#     if 'registered' in session:
#         # User is already registered, render the login template
#         return render_template('login.html')
#     else:
#         # User is not registered, render the register template
#         return render_template('register.html')





from flask import render_template
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Process form data and perform authentication
        username = form.username.data
        password = form.password.data
        # Perform user authentication logic here

        # Redirect to a different page after successful login
        return redirect('/dashboard')

    return render_template('login.html', form=form)




@auth.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
            flash('We appreciate the feedback, be on the lookout for our response', category='success')
    return render_template("contact.html", current_user=current_user)


@auth.route('/logout')
def logout():
	logout_user()
	flash('Logout successful')
	return redirect(url_for('aven.index'))













