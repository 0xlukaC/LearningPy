from flask import Flask, render_template, request, send_file, send_from_directory
import os

app = Flask(__name__)
# app = Flask(__name__, template_folder='your/custom/template/folder')


@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    print("hai")
    product = num1 * num2
    return render_template(
        "./product.html", product=product
    )  # remove the ./templates/ because thats where it looks


books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
]


@app.route("/list")
def listbooks():
    return render_template("./list.html", books=books)


@app.route("/<string:color1>")
def colours(color1):
    return render_template("./response.html", color=color1)


@app.route("/image.png")
def image():
    return send_file("./static/image.png")
    # return send_file("./static/index.html")


@app.route("/image")
def page():
    return send_file("./static/index.html")


app.run(debug=True)
