from flask import Flask, render_template, request, redirect
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%m-%d-%Y %H:%M:%S %p")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    sum = int(request.form['strawberry']) + int(request.form['blackberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} for {sum} fruits")
    return render_template("checkout.html", data=request.form, sum=sum, current_time=current_time)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)