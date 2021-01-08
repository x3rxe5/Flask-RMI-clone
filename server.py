import socket,os,sys
from dotenv import load_dotenv
from pathlib import Path
import subprocess

env_path = Path(".")/'.env'
load_dotenv(dotenv_path=env_path)

host = os.getenv("host")
port = int(os.getenv("port"))
buffer = int(os.getenv("buffer_size"))
msg_code = ""
msg_data = ""




def echo_message():
    return "Hello world"

# You can implement the whole function over here

def message_handler(msg):
    switcher = {
        "terminate":"break",
        "echo":echo_message()
    }
    return switcher.get(msg,"nothing")

def server_start(addr):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind(addr)
        sock.listen()
        print("[+] server has started on port "+str(port))
        conn,addr = sock.accept()
        with conn:
            print("[>] client online ",addr)
            while True:
                try:
                    data = conn.recv(buffer)
                    data = data.decode("utf-8")
                    msg_data = message_handler(data)
                    msg_code = str(200)
                    final_message = msg_code+" "+msg_data
                    conn.sendall(final_message.encode("utf-8"))

# Exception Handling                
                except Exception as err:
                    print("This specific error occured -> "+str(err))
                    msg_code = str(404)
                    msg_data = "error occured -> "+str(err)
                    final_message=msg_code+msg_data
                    conn.sendall(final_message.encode("utf-8"))
# How can i specifically raise this error -> 
                except KeyboardInterrupt:
                    sock.close()
                    break
        sock.close()


if __name__ == "__main__":
    addr = (host,port)
    server_start(addr)
