from flask import Flask ,render_template 

app = Flask(__name__)

# @app.route('/')
# def start():

#     return render_template('index1.html',result = None )

@app.route("/",methods=["GET","POST"])

def planet ():
    
    result = {
        "1" :"hello"    
    }
    return render_template("index1.html",output=result)

if __name__ =="__main__":
    app.run(debug=True,port = 3021)