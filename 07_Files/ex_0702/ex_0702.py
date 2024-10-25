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
        asking_for_a_file_name()
    searching_line(fhand)

def searching_line(file_handle):
    for line in file_handle:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            lines_counter()
            #line.find(':') + 1
            # cases: there are a blanc space before the number, there are a letter before the number
            #       there aren't blanc after the number, there a space after
            # There is a way, slicing testing each index after the strig until get a traceback, and the index to
            # convert to float will be ErrorIndex-1 at the end

def lines_counter():
    global counter
    counter += 1
    return counter


#------------------------
# MAIN
#------------------------
asking_for_a_file_name()
