from flask import Flask,render_template,request,jsonify,redirect,url_for
import json 

app  = Flask(__name__)

PORT = 5000
filename="data.json"

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route("/display", methods=["GET","POST"]) 

def startpy():

    return render_template("index.html",data = filename)


@app.route('/process',methods= ['GET','POST'])
def process():
        url = request.form.get('url')
        API = request.form.get('AIP_key')
        tips = request.form.get('tips')
        cl=tips.split()
        
        data={"key1":url,"key2":API,"key3":cl}
        save(data)

        return render_template('display.html',data=getdata())

def save(data):
    print(f"..saving {filename}")
    with open(f"{filename}", 'w') as file_obj:
        json.dump(data,file_obj)
    print("..saved")

def getdata():
    
    with open(filename) as local_file:
        data = json.load(local_file)
    return data

def delete(id):
     
    f = f'user/{id}'
    if os.path.exists(f):
         os.remove(f)
    
    return render_template('delete.html')

def edit(id):

    f= open(f'user/{id}',)
    data =json.load(f.read())

    result =view_item()

    return render_template("edit.html",result =data,results = result)



if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port = PORT)
