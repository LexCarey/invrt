from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Color():
    def __init__(self, data):
        self.id = data["id"]
        self.product_id = data["product_id"]
        self.color = data["color"]
        self.hex = data["hex"]
        self.xs_stock = data["xs_stock"]
        self.s_stock = data["s_stock"]
        self.m_stock = data["m_stock"]
        self.l_stock = data["l_stock"]
        self.xl_stock = data["xl_stock"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

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