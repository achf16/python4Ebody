#-------------------------
#   Function definitions
#-------------------------
def chop(l):
    del l[0]
    del l[len(l)-1]

def middle(lst):
    return lst[1:len(lst)-1]

#------------------------
#   Main
#------------------------
while True:
    inp = input('Enter numbers/words separated by a space (write just "done" to end): ')
    if inp == 'done':
        quit()
    inp_list = inp.split()
    if len(inp_list) < 5:
        print('You need at least five separate numbers/words.')
        continue
    print("After splitting:", inp_list)
    chop(inp_list)
    print("After chopping:", inp_list)
    n_l = middle(inp_list)
    print("After middling:", n_l)
    print("After middling, the chop list remains the same:", inp_list)
