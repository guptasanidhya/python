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

    features=[]
    if request.form['sl']!='':
        sl = float(request.form['sl'])
        features.append(sl)
    else:
        sl=np.nan
        features.append(sl)

    if request.form['sw']!='':
        sw = float(request.form['sw'])
        features.append(sw)

    else:
        sw=np.nan
        features.append(sw)

    if request.form['pl']!='':
        pl = float(request.form['pl'])
        features.append(pl)
    else:
        pl=np.nan
        features.append(pl)
    if request.form['pw']!='':
        pw = float(request.form['pw'])
        features.append(pw)
    else:
        pw=np.nan
        features.append(pw)

    final_features=[np.array(features)]
    prediction=model.predict(final_features)
    print(features)
    output=prediction[0]

    return render_template('index.html',prediction=output)
if __name__ == "__main__":
    app.run(debug=True)