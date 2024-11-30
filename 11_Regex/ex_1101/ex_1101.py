#--------------------------------------------
#   Global definitions and libraries
#--------------------------------------------
import re
#--------------------------------------------
#   Function definition
#--------------------------------------------
def init():
    while True:
        rgx_entry = input('Enter a regular expression or "done" to finish: ')
        if rgx_entry.lower() == 'done': quit()
        if not len(rgx_entry): continue
        return rgx_entry

def lines_traverser(rgx):
    count = 0
    fname = 'mbox.txt'
    fhand = open(fname)
    for line in fhand:
        if not len(line.rstrip()) or not re.search(rgx, line): continue
        count +=1
    return fname , count , rgx
#--------------------------------------------
#   Main
#--------------------------------------------
while True:
    f, n , r = lines_traverser(init())
    print(f'{f} had {n} lines that matched {r}')


