from flask import Flask, send_file, render_template
from flask_socketio import SocketIO, emit
import mapGen
from subprocess import Popen
import stream_twitter
import os

heatArray = []
empty = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('mapUpdateEvent')
def generateMap(lat,lon,zoom):
    
    heatArray = mapGen.get_data_points()

    #  53.540996,0-113.497746
    mapGen.createHeatMap(heatArray, lat, lon, zoom )
    emit('mapCreated')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    p=Popen(['python', '.\stream_twitter.py'], shell=True)
    socketio.run(app)