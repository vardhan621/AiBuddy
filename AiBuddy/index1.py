from flask import Flask, request, render_template
import index
import re 
import speech_recognition as sr
listener = sr.Recognizer()
my_dict={}

user_input=""
app= Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html",data=my_dict)
@app.route("/chat",
methods=["POST"])
def submit():
    user_input=""
    action=request.form.get("mic")
    if action=="send":
        user_input=request.form["message"]
    elif action=="mic":
        user_input=user_cmd()
    # index.image_gen("bike")
    while True:
     if user_input.lower() in ["exit", "bye"]:
        break
     botReplay=index.chat_with_gpt(user_input)
     print("ChatBot:",botReplay )
     points=para_point(botReplay)
     mypoints=[]
     for i,point in enumerate(points,1):
       mypoints.append(str(i)+' '+point)
     print(mypoints)
     my_dict[user_input]=mypoints
     
     return render_template("index.html",data=my_dict,my_class="bot_text",My_class="User_text")
     
    
    print(my_dict)
    my_dict[user_input]="Bye i will be there when ever you want my help 😊"
    return render_template("index.html",data=my_dict,my_class="bot_text",My_class="User_text")
def user_cmd():
    command=""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice= listener.listen(source)
            command =listener.recognize_google(voice)
            command= command.lower()
            print(command)

    except Exception as e:
        print("please check your microphone")
        print(f"Error: {e}")
    return command
def para_point(paragraph):
    # Split based on numbers or full stops followed by space
    points = re.split(r'(?:^|\n)\s*\d+[.)](?=\s*[A-Za-z*])', paragraph.strip())
    
    # Clean and filter empty strings
    points = [point.strip() for point in points if point.strip()]
    
    return points

if __name__=='__main__':
    app.run(debug=True)