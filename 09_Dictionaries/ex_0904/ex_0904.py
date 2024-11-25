#   This exercise will have a seemly code of the ex_0903 with a little upgrade: it prints out
#   the maximum key-value pair based on the value.
#   There are two ways:
#       - I already have a sorted key-value list, therefore I just need to print out the index[0]
#         (RAM consumption, file should be smaller than the ram)
#       - The other way is using the max() built-in function over the dictionary.items()
#         (Compute consumption, bigger time)

#-----------------------------------
#   Global definitions and libraries
#-----------------------------------
email_dictionary = dict()
email_dictionary_sorted_list = list()   # for use the key-value pair sorted list outside the sort_dictionary_by_value()
#-----------------------------------
#   Function definitions
#-----------------------------------
def init():
    fname = input("Enter a file name or 'done' to quit: ")
    if fname == 'done': quit()
    if not len(fname): fname = "mbox-short.txt"
    try:
        fhand = open(fname)
    except:
        print("The file could not be opened or doesn't exist")
        return init()
    return fhand

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        dictionary_builder(line.split()[1])

def dictionary_builder(key):
    email_dictionary[key.lower()] = email_dictionary.get(key.lower(), 0) + 1

def sort_dictionary_by_value():
    global email_dictionary_sorted_list
    email_dictionary_sorted_list = sorted(email_dictionary.items(), key=lambda x : x[1], reverse=True)
    for i in range(len(email_dictionary_sorted_list)):
        email_dictionary[email_dictionary_sorted_list[i][0]] = email_dictionary.pop(email_dictionary_sorted_list[i][0])

def max_value_using_sorted_list():
    global email_dictionary_sorted_list
    print(email_dictionary_sorted_list[0][0],email_dictionary_sorted_list[0][1])

def max_value_using_built_in_fx():
    max_value = max(email_dictionary.items(), key= lambda x : x[1])
    print(max_value[0],max_value[1])

#-----------------------------------
#   Main
#-----------------------------------
while True:
    lines_traverser(init())
    sort_dictionary_by_value()
    max_value_using_sorted_list()
    max_value_using_built_in_fx()