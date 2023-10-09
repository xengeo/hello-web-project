import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# POST /sort-names
#    Body Parameters:
#       names=Joe,Alice,Zoe,Julia,Keiran  
#    Expected response (200 OK):
#    Alice,Joe,Julia,Kieran,Zoe
@app.route('/sort-names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return 'You didnt submit any names', 400
    names = request.form['names']
    if ',' not in names:
        return 'Please provide a comma-separated list of names', 400
    return ','.join(sorted(names.split(',')))




# Request:
# POST /count_vowels
#   With body parameter: test=eee
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return f'There are {count} vowels in "{text}"'


# Request:
# GET /wave
#       With query parameter: name=Leo
@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']
    return f'I am waving at {name}'


# Request:
# POST /submit
#       With body parameters: name=Leo & message=Hello world
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # Leo as a BODY PARAMTER hense request.form instead of request.args
    message = request.form['message'] # Hello world

    # send back a friendly message
    return f'Thanks {name}, you send this message: "{message}"'


# Request:
# GET /hello?name=David
#   With QUERY parameter: name=Leo
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"


# Request:
# POST /goodbye
#   With body parameter: name=Alice
@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

