from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "lokesh" 
    age = "15" 

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():

    return render_template('father.html')

@app.route("/mother")
def mother():

    return render_template('mother.html')

@app.route("/sister")
def sister():

    return render_template('sister.html')

@app.route("/friend")
def friend():

    return render_template('friend.html')

if __name__  ==  '__main__':
    app.run(debug=True)