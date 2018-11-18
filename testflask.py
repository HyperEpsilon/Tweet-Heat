from flask import Flask
from flask import send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/route2/')
def route_2():
    return send_file('icon.png', mimetype='image/png')

if __name__ == "__main__":
    app.run()