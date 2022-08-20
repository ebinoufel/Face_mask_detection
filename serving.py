from flask import Flask
from flask import render_template, request, url_for, redirect, session, make_response, flash
import os

app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.urandom(25)

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == "POST":
        f = request.files['file']
        print(f)
        print(f)

        return redirect(url_for("my_result"))
    #print('asdfghj')
    else:

        return render_template("test.html")
@app.route('/result',methods=['GET','POST'])
def my_result():
    return render_template("final.html")


if __name__ == '__main__':
    app.run(debug=True)
