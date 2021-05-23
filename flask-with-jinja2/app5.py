from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<int:id>",methods=["GET","POST"])
def start (id):

    return render_template('index5.html',name="elakia",p=id)

if __name__ =="__main__":
    app.run(debug=True)