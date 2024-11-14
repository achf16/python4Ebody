#------------------------------------
#   Global definitions and Libraries
#------------------------------------
counter_From_lines = 0
#------------------------------------
#   Function definitions
#------------------------------------
def init():
    fname = input('Enter file name  or "done" to finish: ')
    if fname == 'done': quit()
    try:
        fhand = open(fname)
    except:
        print("Invalid file name")
        return init()
    return fhand

def file_lines_traverser(fh):
    global counter_From_lines
    for line in fh:
        if not line.startswith('From '): continue
        lsplited = line.split()
        counter_From_lines += 1
        print(lsplited[1])

#------------------------------------
#   Main
#------------------------------------
while True:
    file_lines_traverser(init())
    print('There are ' + str(counter_From_lines) + ' lines in the file with From as the first word.\n')