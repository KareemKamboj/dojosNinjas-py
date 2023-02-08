from sqlite3 import connect
from Flask_app.config.mysqlconnection import connectToMySQL
from Flask_app import DATABASE
from Flask_app.models import ninjas_model

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row in results:
            dojo_instance = cls(row)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            dojo_instance = cls(results[0])
            return dojo_instance
        return False

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = 'SELECT * FROM Dojos JOIN Ninjas ON Dojos.id = Dojos_id WHERE Dojos.id = %(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("==============================")
        print(results)
        print("==============================")
        if len(results) > 0:
            dojo_instance = cls(results[0])
            ninjas_list = []
            for row_from_db in results:
                ninjas_data = {
                    'id':row_from_db['Ninjas.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db['last_name'],
                    'age': row_from_db['age'],
                    'created_at': row_from_db['created_at'],
                    'updated_at': row_from_db['updated_at'],
                    'Dojos_id': row_from_db['Dojos_id']
                }
                ninja_instance = ninjas_model.Ninjas(ninjas_data)
                ninjas_list.append(ninja_instance)
            dojo_instance.ninjas = ninjas_list
            return dojo_instance
        return False

    @classmethod
    def delete(data):
        query = "DELETE FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query)
        return results