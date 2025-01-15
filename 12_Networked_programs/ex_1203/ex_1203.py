#There are many ways to resolve the following problem:
#   - saving the whole document in the secondary memory and repeat the text until 3k characters
#   - saving the document in the primary memory:
#       @ by chunk until 3k
#       @ the whole document and the repeat it until 3k
# We will develop the 3 ways. It's important to take present that:
#   - the white spaces aren't considered like characters
#   - the document's header isn't count for the total characters sum

#------------------------------------
#   Libraries and global definitions
#------------------------------------
import urllib.request, urllib.parse, urllib.error
import os
import re



#------------------------------------
#   Function definitions
#------------------------------------
def init_server_request():
    while True:
        url_2request = input("Write the url to request or 'done' to exit: ")
        if url_2request == 'done': quit()
        elif not len(url_2request): url_2request = "http://data.pr4e.org/romeo.txt"
        try:
            retrv_doc = urllib.request.urlopen(url_2request)
            return retrv_doc
        except:
            print("Invalid url")

def mode_selector():
    while True:
        mode_flag = input("Choose a mode or 'done' to exit:  ")
        if not len(mode_flag): mode_flag = "1"
        match mode_flag:
            case '1': mode1()
            case '2': mode2()
            case '3': mode3()
            case 'done':
                quit()
            case _:
                print("Invalid mode")

def delete_temp_file():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
        print("Deleted temp file successfully\n")
    else:
        print("File not found")

def white_spaces_cleaner(doc):
    doc_without_spaces = re.sub(r'\s+', '', doc)
    # print(doc_without_spaces)
    return len(doc_without_spaces)

def mode1():
    # This case, assumes that the size of the file is less than the size of the primary memory
    requested_doc = init_server_request().read().decode()
    with open("temp.txt", 'w') as fhand:
        fhand.write(requested_doc)
    # with open("temp.txt") as fhand:
    with open("temp.txt", 'r') as fhand:
        content = fhand.read()
        # TODO: clean the white spaces and to loop until 3k
        lenghts = {"doc_len_avoiding_wspace" : white_spaces_cleaner(content), "doc_len_including_wspace" : len(requested_doc)}
        i_range = int(3000/lenghts["doc_len_avoiding_wspace"])
        for i in range(i_range):
            print(content)
        last_index = finding_last_index(lenghts,content, i_range)
        print(content[:last_index])

        print(f'-----------------------------------------------------------------------------\n'
              f'The size of the original retrieved doc is {lenghts["doc_len_avoiding_wspace"]},\n'
              f'but was necessarily print it more time to  complete the 3k characters, without \n'
              f'counting the white spaces like characters\n'
              f'-----------------------------------------------------------------------------')
    delete_temp_file()  # avoiding a trash file on secondary memory at the end of the program

def finding_last_index(len_s,doc,i_rang):
    total_left_character_range = 3000 - len_s["doc_len_avoiding_wspace"]*i_rang
    last_doc_index_for_print = 0
    doc_list = list(doc)
    i = 0
    while last_doc_index_for_print < total_left_character_range:
        if not doc_list[i].isspace(): last_doc_index_for_print += 1
        i += 1
    return i

def mode2():
    #This mode assumes that the overall size of the doc is less than the primary memory
    requested_doc = init_server_request().read().decode()
    lenghts = {"doc_len_avoiding_wspace" : white_spaces_cleaner(requested_doc), "doc_len_including_wspace" : len(requested_doc)}
    range_for_print = int(3000/lenghts["doc_len_avoiding_wspace"])
    for i in range(range_for_print):
        print(requested_doc)
    last_index = finding_last_index(lenghts,requested_doc,range_for_print)
    print(requested_doc[:last_index])

def mode3():
    requested_doc = init_server_request()
    with open("temp.txt", 'w') as fhand:
        for line in requested_doc:
            fhand.write(line.decode())
    with open("temp.txt", 'r') as fhand:
        doc = fhand.read()
        lenghts = {"doc_len_avoiding_wspace" : white_spaces_cleaner(doc), "doc_len_including_wspace" : len(doc)}
        rep_range = int(3000/lenghts["doc_len_avoiding_wspace"])
        for i in range(rep_range):
            print(doc)
        last_index = finding_last_index(lenghts, doc,  rep_range)
        print(doc[:last_index])

#--------------------------------- ---
#   Main
#------------------------------------
while True:
    print("Select a run mode for this program:\n\t"
            "1- Saving the whole document in the secondary memory\n\t"
            "2- Saving the whole document in the primary memory\n\t"
            "3- Saving the document by chunks in secondary memory\n\t"
            "done- to finish")
    mode_selector()
