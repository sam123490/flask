from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/say/<string:phrase>/<int:num>')
def say_phrase(phrase, num):
    return render_template("hello.html", phrase=phrase, num=num)

if __name__=="__main__":
    app.run(debug=True)