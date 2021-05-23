from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():
    return render_template('index1.html',name="elakia")


if __name__ =="__main__":
    app.run(debug=True)