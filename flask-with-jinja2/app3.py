from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():
    user=['Priyanka','Elakia','Vini']
    return render_template('index3.html',name="elakia",members=user)

if __name__ =="__main__":
    app.run(debug=True)
