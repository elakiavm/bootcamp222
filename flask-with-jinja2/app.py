from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():
    return "Hello"

@app.route("/hi",methods=["GET","POST"])
def hello ():
    return '''
    <html>
    <head>
    </head>
    <body>
        <h2> welcome to html </h2>
        <p> this is my page </p>

    </body>
    </html>'''


if __name__ =="__main__":
    app.run(debug=True)