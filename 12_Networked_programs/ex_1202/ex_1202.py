#---------------------------------------
#   Libraries
#---------------------------------------
import socket
import re

character_counter = 0
character_counter_with_white_space = 0
flag_once = True
flag_url_user_req = True
url_server = None
url_2request = None
#---------------------------------------
#   Function definition
#---------------------------------------
def socket_init():
    global flag_url_user_req, url_server, url_2request
    while True:
        if flag_url_user_req:
            url_2request = input("Enter the URL or 'done' to finish: ")
            if url_2request.lower() == 'done': quit()
            if not len(url_2request): url_2request = "http://data.pr4e.org/romeo.txt"
            try:
                url_server = url_2request.split('/')[2]
                # print(url_server)
            except:
                print("Invalid URL")
            flag_url_user_req = False
        try:
            mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mysock.connect((url_server, 80))
            return ("GET " + url_2request + " HTTP/1.0\r\n\r\n").encode(), mysock
        except:
            print("Invalid URL")

def socket_setup(cmd_plus_mysock_tuple):
    global character_counter, character_counter_with_white_space
    mysock = cmd_plus_mysock_tuple[1]
    cmd = cmd_plus_mysock_tuple[0]
    mysock.send(cmd)
    # print("SEND OK")
    #To print the first 3k characters; there are several considerations to take in consideration:
    #   @ White space:
    #       - Are white space considerate character? Yes or No
    #   @ Should I save part, whole or nothing of the document
    #       - Save the whole document and then print until 3k characters
    #           [ Less efficient: same result, more time, and It isn't necessary because the document will be used once]
    #       - Save the document until the len(data) > 3k and then print until 3k characters
    #           [ Because The document will be only read once, It isn't important to save it ]
    #       - Save anything about the document, just print the receiving chunk of data until 3k
    #   @ Save place
    #       - primary memory
    #       - secondary memory
    #I will  use  chunks of the primary memory to print the text until 3k, then
    #I will be continuous counting until the end of the document to print the total number of character
    print_flag = True
    while True:
        data = mysock.recv(1000)
        # print("Receive OK ")
        if len(data) < 1: return character_counter
        cdata = cleaning_white_space(data)
        character_counter += len(cdata)
        character_counter_with_white_space += len(data)
        data_decoded = data.decode()
        if print_flag:
            if character_counter <= 3000:
                print(data_decoded)
                # print("IMPORTANT C_COUNTER:",character_counter)
            else:
                len_of_last_chunck = 3000- (character_counter - len(cdata))
                i = 0
                index_last_character = 0
                while i < len_of_last_chunck:
                    if not data_decoded[index_last_character].isspace():
                        i += 1
                    index_last_character += 1
                print(data_decoded[:index_last_character])
                print_flag = False
                # print("PRINT FLAG 1")
                # print("IMPORTANT C_COUNTER:",character_counter)
                # print("IMPORTANT C_COUNTER:",len(data.decode()[:3000-character_counter]))

def cleaning_white_space(d):
    clean_data = re.sub(r'\s','',d.decode())
    return clean_data
#---------------------------------------
#   Main
#---------------------------------------
while character_counter <= 3000:
    if flag_once:
        total_characters = socket_setup(socket_init())
        print("The total characters in the document is:", total_characters)
        print("----------IMPORTANT--------------")
        print("[But the document will be retrieve as many times as needed to complete 3000 characters].")
        print("[White spaces aren't consider like characters.]")
        print("-------------------------------------------\n")
        flag_once = False
    else:
        socket_setup(socket_init())
