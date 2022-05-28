from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.cart import Cart


#TEMPLATE ROUTES
@app.route('/cart')
def cart():
    if "user_id" in session:
        id = { "id": session["user_id"]}
        cart = Cart.get_cart(id)
        return render_template("cart.html", cart=cart)
    flash("Please create an account or sign-in to view your cart.", "cart")
    return redirect('/account')





#ACTION ROUTES
@app.route('/add-cart', methods=['POST'])
def add_cart():
    product = request.form["name"]
    if "user_id" in session:
        if Cart.validate_cart(request.form):
            data = {
                "size": request.form["size"],
                "quantity": request.form["quantity"],
                "user_id": session["user_id"],
                "product_id": request.form["color"]
            }
            Cart.add_to_cart(data)
            return redirect('/cart')
        return redirect(f'/products/{product}')
    flash("Please create an account or sign-in to add to your cart.", "product")
    return redirect(f'/products/{product}')

@app.route('/remove_from_cart/<int:id>')
def remove_from_cart(id):
    Cart.remove_item_from_cart({ "id": id })
    return redirect('/cart')

@app.route('/update_cart', methods=['POST'])
def update_from_cart():
    data = {
        "id": request.form["id"],
        "quantity": request.form["quantity"]
    }
    Cart.update_item_from_cart(data)
    return redirect('/cart')