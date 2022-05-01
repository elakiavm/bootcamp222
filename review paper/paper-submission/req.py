from flask import Flask,render_template,request, send_from_directory, current_app as app
from flask import send_file
import json
import os 
from pymongo import MongoClient
# from werkzeug.utils import secure_filename
from urllib.request import urlopen

cluster = MongoClient('mongodb+srv://elakia:<password>@cluster0.dyhgo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["Paper_review"]
col = db["Name"]


app  = Flask(__name__)
PORT = 5000
app.config['UPLOAD_FOLDER']='/home/masha/Tact/paper-submission/static/'

#The code below is for uploading the paper and to display the input. It includes the conversion of pdf to web link. 

filename1="data.json"

@app.route("/submit", methods=["GET","POST"]) 
def input1():
    
    return render_template("submit.html")


@app.route("/display1", methods=["GET","POST"]) 
def output():
    # id          =   request.form.get('id')
    title       =   request.form.get('title')
    file        =   request.form.get('file')
    # keywords    =   request.form.get('keywords')
    
    collection.insert_one ({"Tile":title, "File":file})
    for x in collection.find():
    # val=x['P.ID']
    val1=x['Title']
    val2=x['File']
    # val3=x['Keywords']
    result ={
        # 'P.ID' : val,
        'Title' : val1,
        'File' : val2
        # 'Keywords': val3
    }

    # upload_file() 
    # save(data)
    return render_template('display1.html', result= result)

# def upload_file():
#     print("uploading file")
#     if request.method == 'POST':
#       f = request.files['file']
#     f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))    
#     return 'file uploaded successfully'

  
# def save(data):
#     print(f"..saving {filename1}")
#     with open(f"{filename1}", 'w') as file_obj:
#         json.dump(data,file_obj)

#     print("..saved")


# def getdata():
#         with open(filename1 , 'r') as local_file:
#             data = json.load(local_file)
#         return data
        
    
#The below code is for the review form and display of the scores. 

# filename2="/home/masha/Tact/paper-submission/score.json"

@app.route("/review", methods=["GET","POST"]) 
def input2():
    
    return render_template("review.html")

    
@app.route("/display2", methods=["GET","POST"]) 

def score():
    category             =   request.form.get('category')
    context              =   request.form.get('context')
    correct              =   request.form.get('correct')
    contributions        =   request.form.get('contributions')
    clarity              =   request.form.get('clarity')
    overall_score        =   request.form.get('overall_score')


    
    collection.insert_one {"Category":category, "Context":context, "Correct":correct, "Contribution":contributions, "Clarity":clarity, "Overallscore":overall_score }
    for x in collection.find():
    val=x['Category']
    val1=x['Context']
    val2=x['Correct']
    val3=x['Contribution']
    val4=x['Clarity']
    val5=x['Overallscore']

    data ={
        'Category' : val,
        'Context' : val1,
        'Correct' : val2,
        'Contribution': val3,
        'Clarity':val4,
        'Overallscore':val5
    }
    return render_template('display2.html',data= data)


# def save(data):
#     print(f"..saving {filename2}")
#     with open(f"{filename2}", 'w') as file_obj:
#         json.dump(data,file_obj)

#     print("..saved")
    
# def getdata():
#         with open(filename2) as local_file:
#             data = json.load(local_file)
#         return data


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
    