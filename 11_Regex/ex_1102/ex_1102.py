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
        elif not len(fname): fname =  "mbox-short.txt"
        try:
            fhand = open(fname)
            return fhand
        except:
            print("File cannot be opened:", fname)

def lines_traverser(fh):
    numbers = list()
    #rgx = '\s+(\d+[.]?\d?)\s+' # all numbers
    rgx = r'^New Revision:\s+(\d+[.]?\d?)\s+'
    for line in fh:
        if not len(re.findall(rgx,line)): continue
        numbers.extend([float(number) for number in re.findall(rgx,line)])
        # print(numbers)
        # if len(numbers) > 20: quit()
    return sum(numbers), len(numbers)

#------------------------------------------
#   Main
#------------------------------------------
while True:
    total , n = lines_traverser(init())
    print(int(total/n))