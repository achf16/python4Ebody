#--------------------------------------
#   Global definitions and libraries
#--------------------------------------

#--------------------------------------
#   Function definitions
#--------------------------------------
def init():
    while True:
        fname = input('Enter file name or "done" to quit: ')
        if fname == 'done': quit()
        elif len(fname) == 0: fname = "mbox-short.txt"
        try:
            fhand = open(fname)
            return fhand
        except:
            print("File cannot be opened:", fname)

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        dictionary_builder(line.split()[1])

def dictionary_builder(key):
    email_histogram[key.lower()] = email_histogram.get(key.lower(), 0) + 1

def most_repeated_key(d):
    most_repeated_key_tuple = max(d.items(), key=lambda x: x[1])
    return most_repeated_key_tuple
#--------------------------------------
#   Main
#--------------------------------------
email_histogram = dict()
while True:
    lines_traverser(init())
    addr , domain = most_repeated_key(email_histogram)
    print(addr,domain)