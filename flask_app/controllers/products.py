from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.product import Product

#MAIN ROUTES
#TEMPLATE ROUTES
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
    print(products)
    return render_template("drops.html", num=num, products = products)

@app.route('/upcoming-drops')
def upcoming():
    return render_template("upcoming.html")

@app.route('/products/<product>')
def product(product):
    products = Product.get_product_by_name({ "name": product })
    return render_template("product.html", products = products)