from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Picture():
    def __init__(self, data):
        self.id = data["id"]
        self.color_id = data["color_id"]
        self.name = data["name"]
        self.picture_link = data["picture_link"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_pictures_by_color_id(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM pictures WHERE color_id = %(color_id)s;"
        results = mysql.query_db(query, data)
        output = []
        if results:
            for row in results:
                output.append(cls(row))
        return output