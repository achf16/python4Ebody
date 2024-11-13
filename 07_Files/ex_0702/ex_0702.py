#------------------------
#Global definitions
#------------------------
counter = 0
#------------------------
# Fx Definitions
#------------------------
def asking_for_a_file_name():
    fname = input("Enter a file name: ")
    try:
        fhand = open(fname)
    except:
        print(f"Invalid file. {fname} does not exist.")
        return asking_for_a_file_name()
    return fhand

def searching_line(file_handle):
    total = 0
    c = 0
    s = "X-DSPAM-Confidence:"
    index_bfloat = len(s)
    for line in file_handle:
        line = line.strip()
        if line.startswith(s):
            c = lines_counter()
            total += searching_float(line,index_bfloat)
    return total , c

def lines_counter():
    global counter
    counter += 1
    return counter

def searching_float(l, index_bf):
    while l[index_bf] == ' ': index_bf += 1
    index_ff = index_bf + 1
    if l[index_bf] == '0': index_ff += 2
    while float(l[index_bf: index_ff]) == 0: index_ff += 1   #  0.00 case
    try:
        while float(l[index_bf: index_ff]) and index_ff < len(l): index_ff += 1
    except: pass
    return float(l[index_bf : index_ff])

def ave(total_plus_counter):
    return total_plus_counter[0] / total_plus_counter[1]

#------------------------
# MAIN
#------------------------
print('Average spam confidence:', ave(searching_line(asking_for_a_file_name())))