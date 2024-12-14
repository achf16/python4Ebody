#------------------------------------------
#   Global definitions and Libraries
#------------------------------------------
import re
#------------------------------------------
#   Function definitions
#------------------------------------------
def init():
    while True:
        fname = input('Enter file name or "done" to quit: ')
        if fname.lower() == 'done': quit()
        elif not len(fname): fname =  "regex_sum_42.txt"
        try:
            fhand = open(fname)
            return fhand
        except:
            print("File cannot be opened:", fname)

def lines_traverser(fh):
    numbers = list()
    rgx = r'[0-9]+'
    for line in fh:
        if not len(re.findall(rgx,line)): continue
        numbers.extend([float(number) for number in re.findall(rgx,line)])
    return sum(numbers), len(numbers)

#------------------------------------------
#   Main
#------------------------------------------
while True:
    total , n = lines_traverser(init())
    print(int(total))