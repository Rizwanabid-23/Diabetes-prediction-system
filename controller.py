from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")



@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/checkPatient")
def addProd():
    return render_template("base.html")


app.run(debug=True)