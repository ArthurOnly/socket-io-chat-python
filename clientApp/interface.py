from tkinter import Tk, Text, Label, Button, Frame, Scrollbar, VERTICAL
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

        #chat container
        chat_container = Frame(interface, height=60)
        chat_container.pack(fill='x', expand=1)

        ChatBox = Label(chat_container, bg="#eee", justify='left', anchor='sw', padx=16, font=("Arial", 18), height=20)
        ChatBox.pack(fill='x', expand=1)
        self._chat_box = ChatBox
        #end chat container

        input_container = Frame(interface)
        input_container.pack(fill='x')

        ChatInput = Text(input_container, height=2)
        ChatInput.pack(side='left')
        self._text_input = ChatInput

        ChatSend = Button(input_container, text='Enviar', command = self.button_click )
        ChatSend.pack(side='right', fill='both', expand=1)

        self._interface = interface
        threading.Thread(target=self.start_listening).start()
        interface.bind("<KeyPress>", self.press_enter)

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

    def button_click(self, remove_last = False):
        msg = self._text_input.get(1.0, "end-1c")
        if remove_last:
            msg = msg.rstrip(msg[-1])
        if msg:
            self._socket_client.socket.emit('msg', {'msg': msg, 'room': self._socket_client.room, 'author': self._socket_client.username})
            self._text_input.delete(1.0, "end-1c")

    def press_enter(self, key):
        if key.keycode == 13:
            self.button_click(True)
