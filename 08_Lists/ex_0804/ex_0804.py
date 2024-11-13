#-----------------------------------
#   Libraries and Global definitions
#-----------------------------------

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
        if len(words) == 0: continue
        # Here should stay the line traverser with an other for

#-----------------------------------
#   Main
#-----------------------------------
while True:
    inter_line_traverser(init())
