"""My Socket Program (Client Side) """

import socket
import sys
import random

from threading import Thread

from datetime import datetime

import colorama
from colorama import Fore


colorama.init()


colours = [Fore.BLUE, Fore.CYAN, Fore.RED, Fore.YELLOW, Fore.WHITE, Fore.GREEN]

ClientCol = random.choice(colours)

token = "<SEP>"

SHOST = "127.0.0.1"

SPORT = int(sys.argv[1])

s1 = socket.socket()

print("[+] Connecting to {}:{}..".format(SHOST,SPORT))

s1.connect((SHOST, SPORT))


username = input("Enter your username!")

print("[+] Connected! Type Quit to quit.")

def listen_for_msg():
    while True:
        message = s1.recv(1024).decode()
        print("\n{}".format(message))


t1 = Thread(target=listen_for_msg)

t1.daemon = True

t1.start()

while True:

    MsgSend = input()

    if MsgSend.lower() == "quit":
        s1.send(("{} Has Left The Chat Room.".format(username)).encode())
        break

    CurrentDate = datetime.now().strftime('Sent at: %d-%m-%Y %H:%M:%S')

    MsgSend = "{}{} [{}]{}{}{}".format(ClientCol, username, CurrentDate, token, MsgSend, Fore.RESET)

    s1.send(MsgSend.encode())


s1.close()


