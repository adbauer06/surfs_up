# Import flask
from flask import Flask

# Create am app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello world'   

if __name__ == "__main__":
    app.run(debug=True)