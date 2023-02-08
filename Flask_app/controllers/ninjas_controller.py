from Flask_app import app
from flask import render_template, request, session, redirect
from Flask_app.models.dojos_model import Dojos
from Flask_app.models.ninjas_model import Ninjas

@app.route('/ninjas/new')
def new_ninja_form():
    all_dojos = Dojos.get_all()
    return render_template("new_ninja.html", all_dojos = all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def ninja_create():
    Ninjas.create(request.form)
    return redirect(f"/") 
