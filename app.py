"""."""
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    """."""
    return render_template("index.html")


@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    """."""
    if request.method == "GET":
        return render_template("post_add.html")
    elif request.method == "POST":
        print(request.form["content"])
        return render_template("post_add.html")


app.run()
