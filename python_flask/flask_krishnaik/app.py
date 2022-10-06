from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    if score >= 33:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    res = ""
    if score >= 33:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<33:
        result='fail'
    else :
        result='success'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=["POST","GET"])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4
    return redirect(url_for('results', marks=total_score))

if __name__=='__main__':
    app.run(debug=True)
