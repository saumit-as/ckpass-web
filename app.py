from flask import Flask, render_template, request, redirect
import csv
import check_password as ck

app = Flask(__name__)


@app.route('/')
def home():
#     return render_template('index.html')
    return "hi"


@app.route('/submit_form', methods=['POST'])
def submit_form():
    password = (request.form.get("password"))
    cnt = ck.main(password)
    if(cnt):
        res = f"{password} is found {cnt} times!! You should change it."
    else:
        res = f"{password} not found! You are good to go."
    return render_template("test.html", res=res)


if __name__ == "__main__":
    app.run()

''' 
scripts/activate.ps1
$env:FLASK_APP = "server.py"
$env:FLASK_ENV = "development"
flask run '''
