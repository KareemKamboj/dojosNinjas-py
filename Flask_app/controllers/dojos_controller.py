from Flask_app import app
from flask import render_template, request, session, redirect
from Flask_app.models.dojos_model import Dojos

@app.route('/')
def index():
    print("=======================================")
    all_dojos = Dojos.get_all()
    return render_template('index.html', all_dojos = all_dojos)

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = Dojos.get_one_with_ninjas({'id':id})
    return render_template('dojo_show.html', one_dojo=one_dojo)

@app.route('/dojos/create', methods=['post'])
def add_dojo():
    print("found-----------------------------")
    Dojos.create(request.form)
    return redirect('/')

