from flask_app import app, creds
from flask import render_template, redirect, request, session, flash
from flask_app.models.product import Product
from flask_app.models.color import Color
from flask_app.models.picture import Picture
import stripe

stripe.api_key = creds.STRIPE_SECRET_KEY

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    items_in_cart = []
    for item in session['cart']:
        items_in_cart.append({'price': item["stripe_link"], 'quantity': item["quantity"]})
    checkout_session = stripe.checkout.Session.create(
        line_items=items_in_cart,
        mode='payment',
        success_url='http://localhost:5000/success',
        cancel_url='http://localhost:5000/cart',
        shipping_address_collection={
        'allowed_countries': ['US', 'CA'],
        },
        shipping_options=[
            {
            'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 700,
                    'currency': 'usd',
                },
                'display_name': 'First Class',
                'delivery_estimate': {
                    'minimum': {
                        'unit': 'business_day',
                        'value': 5,
                    },
                'maximum': {
                    'unit': 'business_day',
                    'value': 7,
                },
                }
            }
            },
        ],
    )
    return redirect(checkout_session.url, code=303)

#TEMPLATE ROUTES
@app.route('/cart')
def cart():
    if 'cart' not in session:
        session['cart'] = []
    if 'cart_total' not in session:
        session['cart_total'] = "{:.2f}".format(0.00)
    if 'cart_id_counter' not in session:
        session['cart_id_counter'] = 0
    return render_template("cart.html", cart_total=session["cart_total"], cart=session["cart"])

#ACTION ROUTES
@app.route('/add-cart', methods=['POST'])
def add_cart():
    if 'cart' not in session:
        session['cart'] = []
    if 'cart_total' not in session:
        session['cart_total'] = "{:.2f}".format(0.00)
    if 'cart_id_counter' not in session:
        session['cart_id_counter'] = 0
    product = request.form["name"]
    cart_list = session['cart']
    add_to_cart_flag = True
    for item in cart_list:
        if item["name"] == product and item["color"] == request.form["color"] and item["size"] == request.form["size"]:
            item["quantity"] = int(item["quantity"]) + int(request.form["quantity"])
            add_to_cart_flag = False
    if add_to_cart_flag:
        color = Color.get_color_by_name({"color": request.form["color"]})[0]
        back_preview = Picture.get_pictures_by_color_id({"color_id": color["id"]})[0].picture_link
        print("COLOR SIZE LINK VVVVV")
        print(color[request.form["size"] + "_link"])
        cart_list.append({
            "name": product,
            "color": request.form["color"],
            "size": request.form["size"],
            "size_stock": color[request.form["size"] + "_stock"],
            "quantity": int(request.form["quantity"]),
            "picture": back_preview,
            "stripe_link": color[request.form["size"] + "_link"],
            "cart_id": session['cart_id_counter'],
            "price": request.form["price"]
        })
    session['cart_id_counter'] = session['cart_id_counter'] + 1
    session["cart"]=cart_list
    session["cart_total"] = "{:.2f}".format(float(session["cart_total"]) + (float(request.form["price"]) * int(request.form["quantity"])))
    print(session["cart"])
    return redirect('/cart')

@app.route('/clear_cart')
def clear_cart():
    session['cart'] = []
    session['cart_total'] = "{:.2f}".format(0.00)
    session['cart_id_counter'] = 0
    return redirect('/cart')

@app.route('/remove_from_cart/<int:num>')
def remove_from_cart(num):
    counter = 0
    cart_list = session['cart']
    for item in cart_list:
        if item["cart_id"] == num:
            session['cart_total'] = "{:.2f}".format(float(session['cart_total']) - (float(item["price"]) * int(item["quantity"])))
            cart_list.pop(counter)
        counter = counter + 1
    session['cart'] = cart_list
    return redirect('/cart')

@app.route('/update_cart/<int:num>', methods=['POST'])
def update_cart(num):
    if request.form["quantity"] == '0':
        return redirect('/remove_from_cart/' + str(num))
    cart_list = session['cart']
    for item in cart_list:
        if item["cart_id"] == num:
            session['cart_total'] = "{:.2f}".format(float(session['cart_total']) - (float(item["price"]) * int(item["quantity"])))
            item['quantity'] = int(request.form["quantity"])
            session["cart_total"] = "{:.2f}".format(float(session["cart_total"]) + (float(item["price"]) * int(request.form["quantity"])))
    session['cart'] = cart_list
    return redirect('/cart')