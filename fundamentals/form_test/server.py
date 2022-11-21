from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super_secret_password'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['user_name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    print(session)
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)