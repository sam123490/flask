from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'super-secret-password'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_view', methods=['POST'])
def add_view():
    # print("THIS IS WORKING!!! =)")
    # session['view'] = request.form
    total_views = 0
    for i in range(len(session)):
        total_views += 1
    print(total_views)
    # print(session)
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    print("THIS IS ALSO WORKING!!! =)")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)