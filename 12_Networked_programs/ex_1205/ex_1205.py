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
    print("Select the reception mode or 'done' to finish: \n"
            "There are four ways to solve this problem:\n"
            "   1- The first one, consist on:\n"
            "       *   receive the whole doc,\n"
            "       *   store on the secondary memory,\n"
            "       *   to find the \\n\\n pattern, because this is the end of the header,\n"
            "       *   and finally, seek that index and print all after that\n"
            "   2- The other way consist on:\n"
            "       *   receive chunks on the primary memory,\n"
            "       *   traverse the received data until found the first \\n\\n pattern\n"
            "       *   and print from there to the end\n"
            "   3- The third way is a mix of the two above:\n"
            "       *   consist on traverse any received data chunk until found \\n\\n pattern(primary memory)\n"
            "       *   then store all from there to the end on the secondary memory\n"
            "       *   and print\n"
            "   4- The fourth way is a mix of the first two to:\n"
            "       *   consist on save the whole document on the secondary memory,\n"
            "       *   traverse until the pattern \\n\\n\n"
            "       *   write from that index until the end in other temp file\n"
            "       *   and finally print")
    while True:
        mode = input("Write here: ").lower().strip()
        match mode:
            case '1':
                mode1()
                break
            case '2':
                mode2()
                break
            case '3':
                mode3()
                break
            case '4':
                mode4()
                break
            case 'done':
                quit()
            case _:
                print("Invalid mode")

    quit()

    

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

