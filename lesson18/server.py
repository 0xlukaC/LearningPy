from flask import Flask, request, render_template, send_file, send_from_directory

app = Flask(__name__)

d = {}
# d = {"joe": "choc", "william": "straw"}


@app.route("/welcome")
def welcome():
    print("hel")
    return "<h1> welcome </h1>"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        icecream = request.form.get("icecream")
        d[name] = icecream
        print(d)
        return f"{name}' favorite icecream is {icecream}"
        # return redirect(url_for('form')) # or just press back
    return send_file("./public/form.html")


@app.route("/list")
def plist():
    return f"{d}"


@app.route("/<path:subpath>")
def name(subpath):
    print(subpath)
    rn = request.path
    return f"<h1> Hi {rn[1:]}</h1>"


# app.run(debug=True)
app.run()
