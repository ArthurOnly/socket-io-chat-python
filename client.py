import socketio
import sys

def delete_last_line():
    "Deletes the last line in the STDOUT"
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

username = input('Nome de usuario: ')
room = input('Sala: ')

sio = socketio.Client()
sio.connect('http://10.25.2.54:5000')
sio.emit('join', {'username': username, 'room': room})

@sio.on('msg')
def on_message(msg):
    print(msg)

def send(msg):
    sio.emit('msg', {'msg': msg, 'room': room, 'author': username})

while True:
    msg = input()
    delete_last_line()
    send(msg)