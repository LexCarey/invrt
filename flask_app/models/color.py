from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Color():
    def __init__(self, data):
        self.id = data["id"]
        self.product_id = data["product_id"]
        self.color = data["color"]
        self.hex = data["hex"]
        self.XS_stock = data["XS_stock"]
        self.S_stock = data["S_stock"]
        self.M_stock = data["M_stock"]
        self.L_stock = data["L_stock"]
        self.XL_stock = data["XL_stock"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.XS_link = data["XS_link"]
        self.S_link = data["S_link"]
        self.M_link = data["M_link"]
        self.L_link = data["L_link"]
        self.XL_link = data["XL_link"]

    @classmethod
    def get_colors_by_product_id(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM colors WHERE product_id = %(product_id)s;"
        results = mysql.query_db(query, data)
        output = []
        if results:
            for row in results:
                output.append(cls(row))
        return output

    @classmethod
    def get_color_by_name(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM colors WHERE color = %(color)s;"
        return mysql.query_db(query, data)