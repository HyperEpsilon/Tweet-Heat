from flask import Flask, send_file, render_template
from flask_socketio import SocketIO, emit
import mapGen


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('mapUpdateEvent')
def generateMap():
    mapGen.createHeatMap()
    emit('mapCreated')

    def show_map():
        return flask.send_file('/maps/map.html')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app)