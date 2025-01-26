#-------------------------------------
#   Libraries and global definitions
#-------------------------------------
import socket
import re
#-------------------------------------
#   Function definitions
#-------------------------------------
def socket_init():
    while True:
        url_2request = input("Write an URL or 'done' to finish: ").lower().strip()
        if url_2request == 'done': quit()
        elif not len(url_2request.strip()): url_2request = "http://data.pr4e.org/romeo.txt"
        server = server_separator(url_2request)
        if server is None:
            print("Server not found")
            continue
        port = 80
        try:
            # print(server)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((server, port))
            cmd = f'GET {url_2request} HTTP/1.0\r\n\r\n'.encode()
            sock.send(cmd)
            return sock
        except:
            print("Connection failed")


def server_separator(url):
    s = re.match(r'https?://([a-z][a-z0-9_]+.+[.][a-z]+)/',url)
    return s.group(1)

def recv_process(mysock):
    #TODO: OS libraries for clean temp file

    #There are four ways of solve this problem:
    #   - The first one, consist on:
    #       *   receive the whole doc,
    #       *   store on the secondary memory,
    #       *   to find the \n\n pattern, because this is the end of the header,
    #       *   and finally, seek that index and print all after that
    #   - The other way consist on:
    #       *   receive chunks on the primary memory,
    #       *   traverse the received data until found the first \n\n pattern
    #       *   and print from there to the end
    #   - The third way is a mix of the two above:
    #       *   consist on traverse any received data chunk until found \n\n pattern(primary memory)
    #       *   then store all from there to the end on the secondary memory
    #       *   and print
    #   - The fourth way is a mix of the first two to:
    #       *   consist on save the whole document on the secondary memory,
    #       *   traverse until the pattern \n\n
    #       *   write from that index until the end in other temp file
    #       *   and finally print

    

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()

#-------------------------------------
#   Main
#-------------------------------------
while True: recv_process(socket_init())

