from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Product():
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.price = data["price"]
        self.drop_num = data["drop_num"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_products_by_drop(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM products WHERE drop_num = %(drop_num)s;"
        results = mysql.query_db(query, data)
        output = []
        if results:
            for row in results:
                output.append(cls(row))
        return output

    @classmethod
    def get_product_by_name(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM products WHERE name = %(name)s;"
        results = mysql.query_db(query, data)
        output = []
        if results:
            for row in results:
                output.append(cls(row))
        return output

    @classmethod
    def get_product_by_name_color(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM products WHERE name = %(name)s AND color = %(color)s;"
        return mysql.query_db(query, data)