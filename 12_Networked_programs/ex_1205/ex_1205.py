#-------------------------------------
#   Libraries and global definitions
#-------------------------------------
import socket
import re
import os


#-------------------------------------
#   Function definitions
#-------------------------------------
def socket_init():
    while True:
        url_2request = input("Write an URL or 'done' to finish: ").lower().strip()
        if url_2request.lower().strip() == 'done': quit()
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
    s = re.match(r'https?://([a-z].+[.][a-z]+)/',url)
    return s.group(1).lower()

def recv_process(my_s):
    #TODO: OS libraries for clean temp file
    # noinspection SqlNoDataSourceInspection
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
                mode1(my_s)
                break
            case '2':
                mode2(my_s)
                break
            case '3':
                mode3(my_s)
                break
            case '4':
                # mode4()
                break
            case 'done':
                quit()
            case _:
                print("Invalid mode")

def mode1(mysocket):
    with open("temp.txt","w") as fhand:
        while True:
            data = mysocket.recv(1024).decode()
            data = data.replace("\r\n","\n")
            if len(data) < 1: break
            fhand.write(data)
    with open("temp.txt","r") as fhand:
        data = fhand.read()
        data_temp= data[300:370]
        last_index_of_the_header = data.find("\n\n")+2
        print(data[last_index_of_the_header:])
    delete_temp_file()
    mysocket.close()

def mode2(mysocket):
    # It's important to keep in mind the case when the first \n is in a chunk
    # and the second one on the next chunk
    second_state_flag = 0  # The second state is the free running
    separate_nn_flag = 0  # if this flag is equal to two, means that the \n\n are separate in two different chunks
    header_end_founded = 0  # this flag is 1 when \n\n is founded
    while True:
        data = mysocket.recv(50).decode()
        data = data.replace("\r\n", "\n")
        if len(data) < 1: break

        if  second_state_flag == 0:
            # print(data)
            # Case when both \n\n are at the same chunk
            header_last_index = data.find("\n\n")
            # print(header_last_index)
            if header_last_index != -1:
                print(data[data.find("\n\n")+2:], end="")
                second_state_flag = 1
                header_end_founded = 1
                continue

            # case when the \n\n are at different chunks
            if header_end_founded == 0:
                if data.endswith("\n") and separate_nn_flag == 0 :
                    separate_nn_flag += 1
                    # print("encontrada la primera")
                    continue
                if data.startswith("\n") and separate_nn_flag == 1:
                    print(data[1:])
                    # print("encontrada la segunda")
                    second_state_flag = 1
                else: separate_nn_flag = 0
        if second_state_flag:
            print(data, end = "")

def mode3(mysocket):
    buffer = ""
    buffer_flag = 1
    while True:
        data = mysocket.recv(100).decode()
        data = data.replace("\r\n", "\n")
        if len(data) < 1: break
        if buffer_flag:
            buffer += data
        data_index = buffer.find("\n\n")
        if data_index == -1: continue
        if buffer_flag:
            with open("temp.txt", "w") as fhand:
                fhand.write(buffer[data_index + 2:])
            buffer_flag = 0
        else:
            with open("temp.txt","a") as fhand:
                fhand.write(data)
        if len(buffer) > 16000: buffer = ""
    with open("temp.txt","r") as fhand:
        data = fhand.read()
        print(data)
    delete_temp_file()
    mysocket.close()



def delete_temp_file():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
        # print("Deleted temp file successfully\n")
    else:
        print("File not found")

#-------------------------------------
#   Main
#-------------------------------------
while True: recv_process(socket_init())

