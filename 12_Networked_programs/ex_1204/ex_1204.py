#-------------------------------------
#   Libraries and Global definitions
#-------------------------------------
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#-------------------------------------
#   Function definitions
#-------------------------------------
def init():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    while True:
        url = input('Enter an URL or "done" to finish: ')
        if url.lower().strip() == 'done': quit()
        elif not len(url): url = "https://docs.python.org"
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except:
            print("Invalid URL.")

def tag_separator(s):
    tags = s("p")
    counter = 0
    for tag in tags:
        counter += 1
    print("There are", counter, "<p> tags.")
#-------------------------------------
#   Main
#-------------------------------------
while True: tag_separator(init())