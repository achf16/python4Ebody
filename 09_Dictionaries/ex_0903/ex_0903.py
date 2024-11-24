#-----------------------------------
#   Global definitions and libraries
#-----------------------------------

#-----------------------------------
#   Function definitions
#-----------------------------------
def init():
    fname = input("Enter a file name or 'done' to quit: ")
    if fname == 'done': quit()
    if len(fname) < 1: fname = 'mbox-short.txt'
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened or does not exist!")
        return init()
    return fhand

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        dictionary_builder(line.split()[1])

def dictionary_builder(key):
    email_dictionary[key.lower()] = email_dictionary.get(key.lower(), 0) + 1

def sort_dictionary_by_value(dictionary):
    sorted_dictionary_list = sorted(dictionary.items(), key=lambda x : x[1], reverse=True)
    for i in range(len(sorted_dictionary_list)):
        email_dictionary[sorted_dictionary_list[i][0]] = email_dictionary.pop(sorted_dictionary_list[i][0])
#-----------------------------------
#   Main
#-----------------------------------
email_dictionary = dict()
lines_traverser(init())
sort_dictionary_by_value(email_dictionary)
print(email_dictionary)