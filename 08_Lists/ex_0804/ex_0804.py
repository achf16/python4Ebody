#-----------------------------------
#   Libraries and Global definitions
#-----------------------------------
import re
uniq_list = list()

#-----------------------------------
#   Function definitions
#-----------------------------------
def init():
    fname = input('Enter a file name or "done" to quit: ')
    if fname == 'done': quit()
    try:
        fhand = open(fname)
    except:
        print("The file doesn't exist")
        return init()
    return fhand


def inter_line_traverser(fh):
    for line in fh:
        words = line.split()
        if len(words) == 0: continue    # empty line
        line_traverser(words)

def line_traverser(w):
    global uniq_list
    for word in w:
        word = re.sub(r'\W', '', word)
        print(word)
        if word.lower() in uniq_list: continue
        uniq_list.append(word)

#-----------------------------------
#   Main
#-----------------------------------
while True:
    # TODO: the list should be sorted and printed
    inter_line_traverser(init())
    uniq_list.sort()
    print(uniq_list)
