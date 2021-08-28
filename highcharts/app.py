from flask import Flask,render_template, jsonify, request
import random
import json
import business


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3000/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = business.get_data()


    return jsonify(result)

'''
http://0.0.0.0:3000/api/add
http://0.0.0.0:3000/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

    Comedian_name       = request.values.get('Comedian_name')
    Film_no             = request.values.get('Film_no ')

    result = {
        'Comedian_name'          : Comedian_name,
        'Film_no'           : Film_no
    }
    result_data = business.add_row(Comedian_name, Film_no)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)