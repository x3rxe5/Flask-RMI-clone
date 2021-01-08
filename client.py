import socket,sys,os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path("./")/'.env'
load_dotenv(dotenv_path=env_path)

host = os.getenv("host")
port = int(os.getenv("port"))
buffer = int(os.getenv("buffer_size"))


def client_start(addr):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect(addr)
        while True:
            inp = str(input("Enter a method to provoke -> "))
            sock.sendall(inp.encode("utf-8"))

            recv_message = sock.recv(buffer)
            recv_message = recv_message.decode("utf-8")
            recv_message = recv_message.split(' ')[1]

            # message to recive and print it on screen
            if recv_message == "break":
                break
                sock.close()
            print("Message from Server Method -> "+recv_message)

            print("================================================\n\n")


if __name__ == "__main__":
    addr = (host,port)
    client_start(addr)
