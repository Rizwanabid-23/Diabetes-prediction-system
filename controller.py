from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")



@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/checkPatient")
def addProd():
    return render_template("base.html")


@app.route("/", methods=['POST','GET'])
def patientData():
    data = request.form
    name = data['name']
    age=data['age']
    bmi=data['bmi']
    cholestrol=data['chol']
    heartDisease=data['heart']
    smoker=data['smoker']
    physicalActivity=data['pactivity']
    alcohol=data['alcohol']
    general=data['ghealth']
    mentalHealth=data['mhealth']
    physicalHealth=data['phealth']
    diffWalking=data['walking']
    education=data['education']
    income=data['income']
    bloodPressure=data['bloodpressure']    
    
    return render_template("result.html",name=name,age=age,bmi=bmi,chol=cholestrol)



app.run(debug=True)