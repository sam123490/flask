from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'super-secret-password'

@app.route('/')
def home():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template('index.html')

@app.route('/add_view', methods=['POST'])
def add_view():
    print("THIS IS WORKING!!! =)")
    session["count"] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    print("THIS IS ALSO WORKING!!! =)")
    session["count"] = 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)