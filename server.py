from Flask_app import app
from Flask_app.controllers import dojos_controller, ninjas_controller

if __name__ == "__main__":
    app.run(debug=True)