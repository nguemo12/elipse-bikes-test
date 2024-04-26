import webhook
from config import PORT,HOST
import socketio
import eventlet

socket = socketio.Server(cors_allowed_origins='*')

app = socketio.WSGIApp(socket)



@socket.event
def message(sid, data):
    print('Message:', data)
    socket.emit('response', {'response': 'Message received'}, room=sid)

@socket.event
def getLiveApiData(sid,data=''):
    # getting update station data in realtime
    response = webhook.getAllStations()
    print("Called API")
    socket.emit('api_refresh',{'data':response},room=sid)

if __name__ == '__main__':
    # Run the server using eventlet
    eventlet.wsgi.server(eventlet.listen((HOST, int(PORT))), app)

