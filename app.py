from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():
    return render_template('index1.html')


if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0')