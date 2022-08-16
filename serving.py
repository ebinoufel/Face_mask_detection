from flask import Flask
from flask import render_template, request, url_for, redirect, session, make_response, flash
import os

app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.urandom(25)

@app.route('/',methods=['GET'])

def index():

    return render_template("test.html",message= "hey potato")
    #return 'pott'

if __name__ == '__main__':
    app.run(debug=True)
