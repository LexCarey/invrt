from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.product import Product
from flask_app.models.color import Color
from flask_app.models.picture import Picture
import json

#MAIN ROUTES
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")



#TEMPLATE ROUTES
@app.route('/drops/<int:num>')
def drops(num):
    products = Product.get_products_by_drop({"drop_num": num})
    print("PRODUCTS ARRAY")
    print(products)
    colors = []
    for x in products:
        colors.append(Color.get_colors_by_product_id({"product_id": x.id}))
    print("COLORS ARRAY")
    print(colors)
    pictures = []
    for y in colors:
        for z in y:
            pictures.append(Picture.get_pictures_by_color_id({"color_id": z.id}))
    print("PICTURES ARRAY")
    print(pictures)
    return render_template("drops.html", num=num, products=products, colors=colors, pictures=pictures)

@app.route('/upcoming-drops')
def upcoming():
    return render_template("upcoming.html")

@app.route('/products/<product>')
def product(product):
    products = Product.get_product_by_name({ "name": product })
    colors = Color.get_colors_by_product_id({"product_id": products[0].id})
    pictures = []
    for x in colors:
        pictures.append(Picture.get_pictures_by_color_id({"color_id": x.id}))
    
    return render_template("product.html", products=products, colors=colors, pictures=pictures)