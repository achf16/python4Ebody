#This program consist on to retrieve the following document:
#   http://data.pr4e.org/intro-short.txt
# and then to extract of the header the below values:
#   -   Last-Modified:
#   -   ETag:
#   -   Content-Length:
#   -   Cache-Control:
#   -   Content-Type:
#---------------------------------
#   Libraries and global definitions
#---------------------------------
import socket
import re


#---------------------------------
#   Functions
#---------------------------------
def init_socket():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        doc2request = input("Write an URL or 'done' to finnish")
        if doc2request.lower().strip() == 'done': quit()
        if not len(doc2request.strip()): doc2request = "http://data.pr4e.org/intro-short.txt"
        server2request = extract_server(doc2request)
        if  server2request is None:
            print("Server not found")
            continue
        port = 80
        cmd = ""

def extract_server(d2rqst):
    svr_url = re.match("https?://([a-z].+[.][a-z]+)/")
    if svr_url is None: return None
    return svr_url.group(1).lower()
#---------------------------------
#   Main
#---------------------------------
init_socket()