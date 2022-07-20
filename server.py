from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def connect():
    print('Cliente conectado')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('msg', username + ' has entered the room.', to=room)
    print(username, ' has entered the room.', room)

@socketio.on('msg')
def msg(data):
    dataJ = '{}: {}'.format(data['author'], data['msg'])
    emit('msg', dataJ, to=data['room'])
    print(dataJ)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('msg', username + ' has left the room.', to=room)
    print(username, ' has entered the room.', room)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)