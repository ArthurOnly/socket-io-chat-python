import socketio

class SocketClient:
    username = None
    room = None
    socket = None

    def __init__(self):
        #self.username = input('Nome de usuario: ')
        #self.room = input('Sala: ')
        self.username = 'Arthur'
        self.room = 1
        self.socket = socketio.Client()

    def start(self):
        self.socket.connect('http://10.25.2.65:5000')
        self.socket.emit('join', {'username': self.username, 'room': self.room})

    def close(self):
        self.socket.disconnect()