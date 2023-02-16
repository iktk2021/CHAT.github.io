from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"]) 
def index():
    print(request.method)

    if(request.method=="POST"):
        print("check")
        s=""
        file=open("templates/chat_room/main.txt","r+")
        print(request.form.get("name"))
        file.write(file.read()+"\n"+request.form.get("name")+"-"+request.form.get("Username"))
        file.close()
    file=open("templates/chat_room/main.txt","r+")
    send=file.read().split("\n")
    print(send)
    file.close()

    return render_template("main.html",show=send)

app.run()
