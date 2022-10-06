from flask import Flask,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my first page"

@app.route('/success/<int:score>')
def success(score):
    return " you are passed with "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "you are failed with "+str(score)

@app.route('/results/<int:marks>')
def result(marks):
    result=""
    if marks<33:
        result='fail'
    else :
        result='success'
    return redirect(url_for(result,score=marks))
if __name__ == '__main__':
    app.run(debug=True)