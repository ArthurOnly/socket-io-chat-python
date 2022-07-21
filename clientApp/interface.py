from tkinter import Tk, Text, Label, Button
from socketClient import SocketClient

class Interface:
    _text_input = None
    _socket = None
    _chat_box = None

    _username = None
    _room = None

    def __init__(self, socket : SocketClient):
        interface = Tk()
        self._socket = socket.socket
        self._username = socket.username
        self._room = socket.room

        self._socket.on(event='msg', handler=self.handle_message)

        ChatBox = Label(interface)
        ChatBox.pack()
        self._chat_box = ChatBox

        ChatInput = Text(interface)
        ChatInput.pack()
        self._text_input = ChatInput

        ChatSend = Button(interface, text='Enviar', command = self.button_click )
        ChatSend.pack()

        interface.mainloop()

    def handle_message(self, message):
        print('Recebi')
        self._chat_box.config(text=message)

    def button_click(self):
        print('Envio')
        msg = self._text_input.get(1.0, "end-1c")
        self._socket.emit('msg', {'msg': msg, 'room': 1, 'author': 'Arthur'})
