from flask import Flask,render_template,request
import numpy as np
import pickle
app =Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def index():
    title='iris dataset demo'
    return render_template("index.html",title=title)

@app.route('/predict',methods=['POST'])
def predict():
    features=[]
    f_count=0
    for x in request.form.values():
        if x!='':
            f_count = f_count + 1
            features.append(float(x))
        else:
            features.append(np.nan)
    if f_count>=3:
        final_features=[np.array(features)]
        prediction=model.predict(final_features)

        output=prediction[0]

        return render_template('index.html',prediction=output)
    else:
        return "need atleast 3 features"
if __name__ == "__main__":
    app.run(debug=True)