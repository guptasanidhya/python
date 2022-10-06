from flask import Flask,render_template,request
import numpy as np
import pickle
app =Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
remove=[]
@app.route('/')
def index():
    title='iris dataset demo'
    return render_template("index.html",title=title)

@app.route('/predict',methods=['POST'])
def predict():
    removelist=[]
    features=[]

    if request.form['sl']!='':
        sl = float(request.form['sl'])
        features.append(sl)
    else:
        removelist.append('SepalLengthCm')

    if request.form['sw']!='':
        sl = float(request.form['sw'])
        features.append(sl)
    else:
        removelist.append('SepalWidthCm')

    if request.form['pl']!='':
        pl = float(request.form['pl'])
        features.append(pl)
    else:
        removelist.append('PetalLengthCm')

    if request.form['pw']!='':
        pw = float(request.form['pw'])
        features.append(pw)
    else:
        removelist.append('PetalWidthCm')
    remove=removelist
    print(features)
    print(removelist)
    final_features=[np.array(features)]
    prediction=model.predict(final_features)

    output=prediction[0]

    return render_template('index.html',prediction=output)
if __name__ == "__main__":
    app.run(debug=True)