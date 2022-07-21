import socketio

class SocketClient:
    username = None
    room = None
    socket = None

    def __init__(self):
        self.username = input('Nome de usuario: ')
        self.room = input('Sala: ')

        sio = socketio.Client()
        sio.connect('http://10.25.2.54:5000')
        sio.emit('join', {'username': self.username, 'room': self.room})

        self.socket = sio

#@sio.on('msg')
#def on_message(msg):
#    print(msg)