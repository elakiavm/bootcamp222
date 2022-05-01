from flask import Flask,render_template,request
import pymongo
from pymongo import MongoClient
import json 
from bson import json_util
from bson.json_util import dumps

cluster = MongoClient('mongodb+srv://elakia:<password>@cluster0.dyhgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["Learning"]
collection = db["Challenge"] #collection

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start():
    return render_template('index.html')

@app.route("/submit",methods=["GET","POST"])
def submit():
    name=request.form.get("username")
    desc=request.form.get("short_summary")

    print(name,desc)
    collection.insert_one({ "Name" : name, "Description": desc })
    results=collection.find()
    # print(dumps(results))
    for x in results:
      
        value1=x['Name']
        print(value1)
        value2=x['Description']
        print(value2)

    result={
        'Name':value1,
        'Description':value2
    }
    return render_template('result.html',result = result)



if __name__ =="__main__":
    app.run(debug=True)