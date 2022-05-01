from flask import Flask,  render_template, request 
import pymongo
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://elakia:Kvtohindu@cluster0.dyhgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["hn"]
col = db["room"]

app  = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def startpy():
     
    final = []
    start = []
    all_data = col.find() 
    for entry in all_data:
        con = {}
        con["name"]=entry["country"]
        con["data"] = entry["gold"]
        final.append(con)
     
    print(final)
    return render_template("index.html",myResult = final) 
    

@app.route("/api")
def crud():
    return render_template("crud.html")

@app.route("/update", methods=["POST","GET"])
def update():
    con = request.form.get('country')
    con2 = request.form.get('country2')
    go2 = request.form.get('gold2')
    print(con)
    print(con2)
    print(go2)
    
    col.update_one( 
        {
            "country" : con
            
        }, 
        {
            "$set":{"country" : con2,"gold" : go2}} 
    )

    return render_template('update.html')

@app.route("/delete", methods=["POST","GET"])
def delete():
    con = request.form.get('country')
    go = request.form.get('gold')
    col.delete_one(
        {
            "country" : con,
            "gold" : go
        }
    )
    for x in col.find():
            val=x['country']
            val2=x['gold'] 
    result = {
        'country' : val ,
        'gold' : val2
    } 

    return render_template('delete.html', result = result)

@app.route("/insert", methods=["POST","GET"])
def insert():
    i = 0
    con = request.form.get('type')
    go =  request.form.get('level')
    i = i+1
    house_id = i

    print(con)
    print(go)
    col.insert_one(
        {
            "_id"      : i,
            "room_id"  : i,
            "house_id" : i,
            "type"     : con,
            "level"    : go
        }
    )


    return render_template('insert.html')  
    


if __name__ == "__main__":
    app.run(debug = True)