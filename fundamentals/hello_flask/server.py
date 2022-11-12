from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/starwars')
def starwars():
    return 'I love starwars!!! =)'
@app.route('/hello/<string:name>/<int:num>/<string:user_id>')
def hello(name, num, user_id):
    return f"hello {name}! Your id is {user_id}" * num
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

