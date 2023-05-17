from flask import Flask,render_template
app=Flask(__name__,
          static_url_path="")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def index2():
    return "123"


app.run()