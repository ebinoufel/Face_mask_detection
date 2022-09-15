from flask import Flask
from flask import render_template, request, url_for, redirect, session, make_response, flash
import os
from PIL import Image 
import PIL 
import yolov5.detect as model
app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))
app.secret_key = os.urandom(25)
my_dir=''
def image():
    global my_dir
    print(my_dir)
    return my_dir

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == "POST":
        f = request.files['file']
        print(f)
        print(f)
        f=f.save("input_images/input_image.jpg")
        print(f)
        #os.system("python yolov5/detect.py")
        global my_dir
        my_dir = my_dir + str(model.get_path())
        print( my_dir)
        session['my_dir']=my_dir
        print(session['my_dir'])
        return redirect(url_for("my_result"))
        #, c = session["my_dir"]
    #print('asdfghj')
    else:

        return render_template("test.html")
@app.route('/my_result',methods=['GET','POST'])
def my_result():
        global my_dir
        #k= image()
        #print(k)
        #print(session['my_dir'])
        print('This is the occurence of path in results')
        print(my_dir)
        my_dir = my_dir.replace('\\','/')
        print(my_dir)
    #my_path = model.my_dir
    #if "new_dir" in session :
        #print (c)
        #my_dir=session["my_dir"]
        #print("hello " ,my_dir)
    #print(my_dir +'input_image.jpeg')
        print(my_dir+'/input_image.jpg')
        return render_template("result.html",user_image = my_dir+'/input_image.jpg')
    #else:
        #print("fghjk")


if __name__ == '__main__':
    app.run(debug=True)
