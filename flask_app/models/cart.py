from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import product

class Cart():
    def __init__(self, data):
        self.id = data["id"]
        self.size = data["size"]
        self.quantity = data["quantity"]
        self.user_id = data["user_id"]
        self.product_id = data["product_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_to_cart(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "INSERT INTO cart (size, quantity, user_id, product_id) VALUES (%(size)s, %(quantity)s, %(user_id)s, %(product_id)s);"
        return mysql.query_db(query, data)

    @classmethod
    def get_cart(cls, data):
        query = "SELECT * FROM users JOIN cart ON users.id = cart.user_id LEFT JOIN products ON cart.product_id = products.id WHERE users.id=%(id)s;"
        results = connectToMySQL("invrt_schema").query_db(query, data)
        products = []
        if results:
            for row in results:
                cart = cls({
                    "id": row["cart.id"],
                    "size": row["size"],
                    "quantity": row["quantity"],
                    "user_id": row["user_id"],
                    "product_id": row["product_id"],
                    "created_at": row["cart.created_at"],
                    "updated_at": row["cart.updated_at"]
                })
                product_data = {
                    "id": row["product_id"],
                    "name": row["name"],
                    "color": row["color"],
                    "description": row["description"],
                    "price": row["price"],
                    "drop_num": row["drop_num"],
                    "soldout": row["soldout"],
                    "design": row["design"],
                    "patch": row["patch"],
                    "front_img": row["front_img"],
                    "back_img": row["back_img"],
                    "created_at": row["products.created_at"],
                    "updated_at": row["products.updated_at"],
                }
                cart.product = product.Product(product_data)
                products.append(cart)
        return products

    @classmethod
    def get_cart_id(cls, data):
        mysql = connectToMySQL("invrt_schema")
        query = "SELECT * FROM cart WHERE id=%(id)s;"
        result =  mysql.query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def update_item_from_cart(cls, data):
        mysql = connectToMySQL("invrt_schema")
        cart_item = Cart.get_cart_id(data)
        if cart_item:
            if cart_item.user_id == session["user_id"]:
                if int(data["quantity"]) == 0:
                    print("hello there this is not working!")
                    return Cart.remove_item_from_cart(data)
                query = "UPDATE cart SET quantity=%(quantity)s WHERE id=%(id)s;"
                mysql.query_db(query, data)

    @classmethod
    def remove_item_from_cart(cls, data):
        mysql = connectToMySQL("invrt_schema")
        cart_item = Cart.get_cart_id(data)
        if cart_item:
            if cart_item.user_id == session["user_id"]:
                query = "DELETE FROM cart WHERE id=%(id)s;"
                mysql.query_db(query, data)

    @staticmethod
    def validate_cart(product):
        is_valid = True
        if len(product["color"]) < 1:
            flash("Must select a color.", "product")
            is_valid = False
        if len(product["size"]) < 1:
            flash("Must choose a size.", "product")
            is_valid = False
        return is_valid
