
from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pickle
from datetime import datetime
import json
app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:@localhost/diabetes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Users(db.Model):
    sno=db.Column(db.Integer,primary_key=True,autoincrement=True)
    fullname=db.Column(db.String(25))
    pregnancies=db.Column(db.Float(),nullable=True)
    glucose=db.Column(db.Float(),nullable=True)
    diastolic=db.Column(db.Float(),nullable=True)
    triceps=db.Column(db.Float(),nullable=True)
    insulin=db.Column(db.Float(),nullable=True)
    bmi=db.Column(db.Float(),nullable=True)
    dpf=db.Column(db.Float(),nullable=True)
    age=db.Column(db.Float(),nullable=True)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    negative = db.Column(db.Float())
    positive = db.Column(db.Float())

# def __repr__(self) -> str:
#     return f"{self.fullname}"


@app.route("/")
def index():
        return render_template("index.html")

@app.route('/home')
def home():
    title='Diabetes Diagnoser'
    return render_template("home.html",title=title)

@app.route("/home",methods=["POST","GET"])
def submit():
     if request.method=='POST':
        fullname=(request.form['fullname'])
        entry=Users(fullname=fullname)


        full=f"Know about your Diabetic health, {fullname}"
        return render_template("home.html",fullname=full)



@app.route('/dataset')
def dataset():
    title='Diabetes Diagnoser'
    return render_template("dataset.html",title=title)

@app.route("/aboutus")
def aboutus():
    title='Diabetes Diagnoser'
    return render_template("aboutus.html",title=title)

@app.route('/predict',methods=['POST'])
def predict():

    """    f_count=0
    for x in request.form.values():
        if x!='':
            f_count = f_count + 1
            features.append(float(x))
        else:
            features.append(np.nan)
    if f_count>=3:
        final_features=[np.array(features)]

        entry=Users(pregnancies=features[0],glucose=features[1],diastolic=features[2],triceps=features[3],insulin=features[4],bmi=features[5],dpf=features[6],age=features[7])
        db.session.add(entry)
        db.session.commit()
        prediction=model.predict(final_features)
        prediction_proba=model.predict_proba(final_features)

        output=prediction[0]
        no=prediction_proba[0,0]
        yes=prediction_proba[0,1]
        neg=f"negative chances of having diabetes is {'{0:.0%}'.format(no)}"
        pos=f"Positive chances of having diabetes is {'{0:.0%}'.format(yes)}"
        return render_template('home.html',prediction=output,negative=neg,positive=pos)
    else:
        return "need atleast 3 features"
 """
    features = []
    test=[]
    fullname = (request.form['fullname'])
    if request.form['pregnancies']!='':
        pregnancies=float(request.form['pregnancies'])
        features.append(pregnancies)
        test.append(pregnancies)
    else:
        pregnancies=np.nan
        features.append(pregnancies)
        pregnancies = None
        test.append(pregnancies)

    if request.form['glucose']!='':
        glucose=float(request.form['glucose'])
        features.append(glucose)
        test.append(glucose)
    else:
        glucose=np.nan
        features.append(glucose)
        glucose = None
        test.append(glucose)

    if request.form['diastolic']!='':
        diastolic=float(request.form['diastolic'])
        features.append(diastolic)
        test.append(diastolic)
    else:
        diastolic=np.nan
        features.append(diastolic)
        diastolic = None
        test.append(diastolic)

    if request.form['triceps']!='':
        triceps=float(request.form['triceps'])
        features.append(triceps)
        test.append(triceps)
    else:
        triceps=np.nan
        features.append(triceps)
        triceps = None
        test.append(triceps)

    if request.form['insulin']!='':
        insulin=float(request.form['insulin'])
        features.append(insulin)
        test.append(insulin)
    else:
        insulin=np.nan
        features.append(insulin)
        insulin = None
        test.append(insulin)

    if request.form['bmi']!='':
        bmi=float(request.form['bmi'])
        features.append(bmi)
        test.append(bmi)
    else:
        bmi=np.nan
        features.append(bmi)
        bmi = None
        test.append(bmi)

    if request.form['dpf']!='':
        dpf=float(request.form['dpf'])
        features.append(dpf)
        test.append(dpf)
    else:
        dpf=np.nan
        features.append(dpf)
        dpf = None
        test.append(dpf)

    if request.form['age']!='':
        age=float(request.form['age'])
        features.append(age)
        test.append(age)
    else:
        age=np.nan
        features.append(age)
        age = None
        test.append(age)

    print(features)


    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    prediction_proba = model.predict_proba(final_features)
    output = prediction[0]
    no = prediction_proba[0, 0]
    yes = prediction_proba[0, 1]
    neg = f"negative chances of having diabetes is {'{0:.0%}'.format(no)}"
    pos = f"Positive chances of having diabetes is {'{0:.0%}'.format(yes)}"
    entry = Users(fullname=fullname,pregnancies=test[0], glucose=test[1], diastolic=test[2], triceps=test[3],
                  insulin=test[4], bmi=test[5], dpf=test[6], age=test[7],negative=no,positive=yes)
    db.session.add(entry)
    db.session.commit()
    return render_template('home.html', prediction=output, negative=neg, positive=pos,features=features,
    fullname=fullname,pregnancies=test[0], glucose=test[1], diastolic=test[2], triceps=test[3],
                  insulin=test[4], bmi=test[5], dpf=test[6], age=test[7],test=test)
    
if __name__ == "__main__":
     app.run(debug=True)