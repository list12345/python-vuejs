from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from mysql.connector import connect
from urllib.parse import urlsplit
from models.products import Product
import os
import time

# wait db is up
time.sleep(5)
app = Flask(__name__)
CORS(app)


# todo: cors
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"

    return response


# Connect to database
db_dsn = urlsplit(os.environ.get('DB_DNS'))
db = connect(
    host=db_dsn.hostname,
    user=db_dsn.username,
    password=db_dsn.password,
    database=db_dsn.path.strip('/'),
    port=db_dsn.port
)


@app.get("/")
@cross_origin()
def home():
    return "Have a good day!"


@app.route("/products")
def get_products(page: int = 1):
    limit = 5
    if page >= 1:
        offset = limit * (page - 1)
    else:
        offset = 0
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products LIMIT " + str(limit) + " OFFSET " + str(offset))
    result = cursor.fetchall()
    return jsonify(result)


@app.route("/products", methods=['POST'])
def add_product():
    sql = "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)"
    print(request.get_json())
    js = request.get_json()
    pr = Product(**js)
    val = (pr.name, pr.price, pr.description)
    cursor = db.cursor()
    cursor.execute(sql, val)
    db.commit()
    if cursor.rowcount == 1:
        result = {"success": True}
    else:
        result = {"success": False}
    return jsonify(result)


@app.route("/products/<id>", methods=['PUT'])
@cross_origin()
def update_product(id: int):
    cursor = db.cursor()
    js = request.get_json()
    pr = Product(**js)
    update_fields = pr.update_sql_fields()
    if update_fields != '':
        cursor.execute("UPDATE products SET " + update_fields + " WHERE id= %s", (int(id),))
        db.commit()
        if cursor.rowcount == 1:
            result = {"success": True}
        else:
            result = {"success": False}
    else:
        result = {"success": False, 'error': "Invalid request"}
    return jsonify(result)


@app.route("/products/<id>", methods=['DELETE'])
def delete_product(id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id= %s", (int(id),))
    db.commit()
    if cursor.rowcount == 1:
        result = {"success": True}
    else:
        result = {"success": False}
    return jsonify(result)


@app.route("/products/<id>", methods=['GET'])
def get_product(id: int):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id= %s", (id,))
    result = cursor.fetchone()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
