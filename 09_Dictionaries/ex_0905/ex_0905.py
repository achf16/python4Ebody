#-----------------------------------
#   Global definitions and libraries
#-----------------------------------
domain_histogram = dict()
#-----------------------------------
#   Function definition
#-----------------------------------
def init():
    fname = input("Enter a file name or 'done' to finish: ")
    if fname.lower() == 'done': quit()
    elif not len(fname): fname = "mbox-short.txt"
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened! or does not exist!")
        return init()
    return fhand

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        dictionary_builder(line.split()[1].split('@')[1])

def dictionary_builder(key):
    domain_histogram[key] = domain_histogram.get(key, 0) + 1

def sort_dictionary_by_value():
    domain_histogram_sorted_list = sorted(domain_histogram.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(domain_histogram_sorted_list)):
        domain_histogram[domain_histogram_sorted_list[i][0]] = domain_histogram.pop(domain_histogram_sorted_list[i][0])
#-----------------------------------
#   Main
#-----------------------------------
while True:
    lines_traverser(init())
    sort_dictionary_by_value()
    print(domain_histogram)