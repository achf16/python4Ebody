#---------------------------------------
#   Libraries
#---------------------------------------
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#---------------------------------------
#   Function definitions
#---------------------------------------
def socket_init():
    while True:
        url_requested = input("Enter the URL of the website or 'done' to finish: ")
        if url_requested.lower() == 'done': quit()
        try:
            url = url_requested.split('/')[2]
            print(url)
            mysock.connect((url,80))
            return ("GET " + url_requested + " HTTP/1.0\r\n\r\n").encode()
        except:
            print("Connection failed or file does not exist")

def request_socket(cmd):
    mysock.send(cmd)
    while True:
        data = mysock.recv(1024)
        if len(data)<1:
            break
        print(data.decode(),end="")
    print("\n")

#---------------------------------------
#   Main
#---------------------------------------
while True:
    request_socket(socket_init())
    mysock.close()

