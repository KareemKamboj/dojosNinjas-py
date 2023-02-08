from Flask_app.config.mysqlconnection import connectToMySQL
from Flask_app import DATABASE

class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Dojos_id = data['Dojos_id']

    @classmethod 
    def create(cls, data):
        query = "INSERT INTO Ninjas (first_name, last_name, age, Dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(Dojos_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)