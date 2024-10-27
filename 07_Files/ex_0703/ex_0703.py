#-----------------------------------
# Libraries and global definitions
#-----------------------------------
import re
#-------------------------
# Function Definitions
#-------------------------
def usr_file_name():
    fname = input('Enter a file name: ')
    if fname.lower() == "done": quit()
    try:
        fhand = open(fname)
    except:
        if re.sub(r"\s", "", fname.lower()) == "nanabooboo":
            print("NA NA BOO BOO TO YOU - You have been punk'd!")
            return usr_file_name()
        else:
            print(f"File cannot be opened: {fname}")
            return usr_file_name()
    return fhand, fname

def sub_line_counter(fh):
    counter = 0
    for line in fh:
        if line.strip().startswith("Subject:"): counter += 1
    return counter

#---------------------------
# Main
#---------------------------
f = usr_file_name()
print(f"There were {sub_line_counter(f[0])} subject lines in {f[1]}")
