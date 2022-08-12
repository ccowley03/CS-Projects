"""My Socket Program (Server Side) """

import socket
import sys

from threading import Thread

SHOST = "0.0.0.0"

SPORT = int(sys.argv[1])

token = "<SEP>"

client_socks = list()

s1 = socket.socket()

# Reusable Port
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s1.bind((SHOST, SPORT))

s1.listen(6)

listsize = 0

print("Listening as {}:{}".format(SHOST, SPORT))

def CheckChatRoom(l1):
    global listsize

    listsize = len(l1)
    if listsize <= 1:
        print("{} Person in Chat Room".format(listsize))
    else:
        print("{} People in Chat Room".format(listsize))


def ClientListen(clientsocket):
    global listsize
    while True:
        try:
            message = clientsocket.recv(1024).decode()
            if "Left" in message:
                print("Someone has left the Chat Room")

        except Exception as exp:
            client_socks.remove(clientsocket)
        else:
            message = message.replace(token, ": ")

        for client_socket in client_socks:
            client_socket.send(message.encode())

while True:

    try:
        client_sock, client_addr = s1.accept()

        client_socks.append(client_sock)

    except Exception as exp:
        break

    print("[+] {} connected!,".format(client_addr), end=" ")

    CheckChatRoom(client_socks)

    # Creating a Daemon Thread that ends when the main thread ends
    try:
        t1 = Thread(target=ClientListen, daemon=True, args=(client_sock,))
        t1.start()

    except Exception as exp:
        s1.close()
        break


for client_socket in client_socks:
    client_socket.close()


s1.close()

