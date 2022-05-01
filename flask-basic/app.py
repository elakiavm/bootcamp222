from crypt import methods
from distutils.log import debug
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    result= {
        'name' :"Ram",
        'age'  : 25
    }
    return render_template("index.html",output = result)

if __name__ == "__main__":
    app.run(debug=True)