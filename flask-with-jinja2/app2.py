from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():
    return render_template('index2.html',name="elakia",message="vadilvel !")


if __name__ =="__main__":
    app.run(debug=True)