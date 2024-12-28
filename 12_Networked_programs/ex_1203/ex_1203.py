#There are ways to resolve the following problem:
#   - saving the whole document in the secondary memory and repeat the text until 3k characters
#   - saving the document in the primary memory:
#       @ by chunk until 3k
#       @ the whole document and the repeat it until 3k
# We will develop the 3 ways. It's important to take present that the white spaces aren't considered like characters

#------------------------------------
#   Libraries and global definitions
#------------------------------------
import urllib.request, urllib.parse, urllib.error


#------------------------------------
#   Function definitions
#------------------------------------
def init():
    while True:
        url_2request = input("Write the url to request or 'done' to exit: ")
        if url_2request == 'done': quit()
        elif not len(url_2request): url_2request = "http://data.pr4e.org/romeo.txt"
        try:
            retrv_doc = urllib.request.urlopen(url_2request)
            return retrv_doc
        except:
            print("Invalid url")

def receiving_process(fhand):
    doc = fhand.read()
    print(doc)


#--------------------------------- ---
#   Main
#------------------------------------
while True:
    url_requested = init()
