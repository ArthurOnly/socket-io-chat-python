from tkinter import Tk, Text, Label, Button, Frame
from socketClient import SocketClient
import threading
import sys

class Interface:
    _interface = None
    _text_input = None
    _socket = None
    _chat_box = None

    _username = None
    _room = None

    def __init__(self, socket : SocketClient):
        interface = Tk()
        interface.geometry('800x600')

        self._socket_client = socket
        self._username = socket.username
        self._room = socket.room

        ChatBox = Label(interface, bg="#eee")
        ChatBox.pack(fill='both', expand=1)
        self._chat_box = ChatBox

        input_container = Frame(interface)
        input_container.pack(fill='x')

        ChatInput = Text(input_container, height=2)
        ChatInput.pack(side='left')
        self._text_input = ChatInput

        ChatSend = Button(input_container, text='Enviar', command = self.button_click )
        ChatSend.pack(side='right', fill='both', expand=1)

        self._interface = interface
        threading.Thread(target=self.start_listening).start()

    def start(self):
        self._interface.mainloop()
        self._socket_client.close()

    def start_listening(self):
        print('Start listening')
        self._socket_client.socket.on(event='msg', handler=self.handle_message)

    def handle_message(self, message):
        msgs = self._chat_box.cget("text")
        msgs = msgs+'\n'+message
        self._chat_box.config(text=msgs)

    def button_click(self):
        msg = self._text_input.get(1.0, "end-1c")
        self._socket_client.socket.emit('msg', {'msg': msg, 'room': 1, 'author': 'Arthur'})
