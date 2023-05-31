# contain all the routes
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
from api.models.data import Region, State, Lga
from api.utils.utils import db

views = Blueprint("views", __name__)


@views.route("/")
def index():
    articles = Region.query.all()
    return render_template("index.html", user=current_user, articles=articles)




# about route displays info about the page
@views.route('/about')
def about():
	return render_template('about.html')


@views.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('We appreciate the feedback, be on the lookout for our response',
                category='success')
    return render_template("contact.html", current_user=current_user)


# @views.route("/article/<email>")
# @login_required
# def aricles(email):
#     user = User.query.filter_by(email=email).first()

#     if not user:
#         flash('No user with that email exists.', category='error')
#         return redirect(url_for('index'))

#     aricles = user.aricles
#     return render_template("aricles.html", user=current_user, aricles=aricles, email=email)






