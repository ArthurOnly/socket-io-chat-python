import socketio

username = input('Nome de usuario: ')
room = input('Sala: ')

sio = socketio.Client()
sio.connect('http://10.25.2.65:5000')
sio.emit('join', {'username': username, 'room': room})

@sio.on('msg')
def on_message(msg):
    print(msg)

def send(msg):
    sio.emit('msg', {'msg': msg, 'room': room, 'author': username})

while True:
    msg = input()
    send(msg)