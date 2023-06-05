# contain all the routes
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
from models.users import User
from models.data import Region, State, Lga



views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.html")

def get_states(region_id):
    states = State.query.filter_by(region_id=region_id).all()
    return states

def get_lgas(state_id):
    lgas = Lga.query.filter_by(state_id=state_id).all()
    return lgas

@views.route("/states/<int:region_id>")
def states(region_id):
    states = get_states(region_id)
    context = {
        'states': states
    }
    return render_template("states.html", user=current_user, context=context)

@views.route("/lgas/<int:state_id>")
def search(self):
    q = request.args.get('q')
    if q:
        lgas = Lga.query.filter(Lga.name.contains(q)).all()
    else:
        lgas = Lga.query.all()
    return render_template("index.html", lgas=lgas)




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






