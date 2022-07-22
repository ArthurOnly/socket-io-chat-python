from interface import Interface
from socketClient import SocketClient
import threading
import asyncio

socket = SocketClient()
gui = Interface(socket)

socket.start()
gui.start()