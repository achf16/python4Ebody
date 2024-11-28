#-------------------------------------
#  Global definitions and libraries
#-------------------------------------
import re
import string

letter_histogram = dict()
#-------------------------------------
#   Function definitions
#-------------------------------------
def init():
    while True:
        fname = input('Enter file name or "done" to quit: ')
        if fname == 'done': quit()
        elif not len(fname): fname = "mbox-short.txt"
        try:
            fhand = open(fname)
            return fhand
        except:
            print("File cannot be opened or does not exist.")

def lines_traverser(fh):
    for line in fh:
        # line = line.translate(str.maketrans('', '', string.punctuation + string.whitespace + '0123456789'))   #Way 1
        line = re.sub(r'[^a-zA-Z]', '', line)   #Way 2
        line = list(line.lower())
        if not len(line): continue
        # print(line)
        for l in line:
            dictionary_builder(l)

def dictionary_builder(key):
    letter_histogram[key] = letter_histogram.get(key, 0) + 1

def sort_letter_by_value(d):
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    #This part isn't necessary to print the sorted dictionary, but it leaves the dictionary sorted
    for i in range(len(sorted_d)):
        letter_histogram[sorted_d[i][0]] = letter_histogram.pop(sorted_d[i][0])

    return sorted_d
#-------------------------------------
#   Main
#-------------------------------------
while True:
    lines_traverser(init())
    for l , v in sort_letter_by_value(letter_histogram):
        print(l, v)