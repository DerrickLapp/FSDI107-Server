from flask import Flask, request, render_template
import json
from http import HTTPStatus
from config import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app) #Warning: This disables CORS policy


# End point of API
@app.get("/")
def home():
    return "Hello, from Flask."

# @app.post("/")
# @app.put("/")
# @app.patch("/")
# @app.delete("/")

@app.get("/test")
def test():
    return "This is another endpoint."

# This is a JSON implementation
@app.get("/api/about")
def about():
    name = {"name": "Derrick test"}
    return json.dumps(name)

@app.get("/about-me")
def about_me():
    user_name = "Derrick"
    return render_template("about-me.html", name=user_name)

products = []

def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


# GET all products
@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for product in cursor:
        products_db.append(fix_id(product))
    return json.dumps(products_db), HTTPStatus.OK


# POST a product
@app.post("/api/products")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)
    return json.dumps(fix_id(product))

########################################################################
########################### COUPON CODES ###############################
########################################################################


#Post to coupons
@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

#Get from coupons
@app.get("/api/coupons")
def get_coupons():
    coupons_db = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        coupons_db.append(fix_id(coupon))
    return json.dumps(coupons_db), HTTPStatus.OK









###### Other End Points #######



# PUT a product
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Update the product with index {index}.")
    if 0<= index < len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist.", 404


# DELETE a product
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"Delete the product with index {index}")
    if index >= 0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product), 200
    else:
        return "That index does not exist.", HTTPStatus.NOT_FOUND
    return "Product Deleted"

# Endpoint that shows List Length
@app.get("/api/products/count")
def product_counter():
    products_db = []
    cursor = db.products.find({})
    for product in cursor:
        print("product", product)
        products_db.append(fix_id(product))
    return "There are " + str(len(products_db)) + " product(s) in the List, currently."

# Endpoint that tallies specific categories
@app.get("/api/products/<category>")
def cata_counter(category):
    products_db = []
    cursor = db.products.find({})
    for product in cursor:
        products_db.append(fix_id(product))
    counted_category = 0
    for products_db in products_db:
        if products_db['category'] == category:
            counted_category += 1
    return "There are " + str(counted_category) + " items in the category: " + category

app.run(debug=True)