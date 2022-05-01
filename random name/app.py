import random 
from flask import Flask, app, render_template, request
app=Flask(__name__)

cnl=[]
listOriginal=[]
listRandom=[]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def get_values():
    n=request.form["count"]
    num=int(n)

    cnl=request.form["objects"]
    listOriginal=cnl.split()

    # print(random(listOriginal))

    listRandom=random.sample(listOriginal,num)
    # print(listOriginal)
    # print(listRandom)

   
    return render_template('result.html',randomlist=listRandom)

if __name__=='__main__':
    app.run(debug=True)



