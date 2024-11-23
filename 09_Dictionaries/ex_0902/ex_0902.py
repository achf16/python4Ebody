#-----------------------------------
#   Global definitions and libraries
#-----------------------------------
#-----------------------------------
#   Function definitions
#-----------------------------------
def init():
    fname = input("Enter a file name or 'done' to finish:")
    if fname == 'done': quit()
    elif len(fname) == 0: fname = 'mbox-short.txt'
    try:
        fhand = open(fname)
    except:
        print("File doesn't exist")
        return init()
    return fhand

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        line = line.split()
        days_week[line[2].lower()]= days_week.get(line[2].lower(),0)+1

def sort_dictionary_by_value():
    days_week_sort_list = sorted(days_week.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(days_week_sort_list)):
        days_week[days_week_sort_list[i][0].capitalize()] = days_week.pop(days_week_sort_list[i][0])
#-----------------------------------
#   Main
#-----------------------------------
days_week = dict()
lines_traverser(init())
sort_dictionary_by_value()
print(days_week)