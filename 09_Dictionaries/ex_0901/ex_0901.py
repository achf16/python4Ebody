#------------------------------------
#   Global definitions and libraries
#------------------------------------
import re
#------------------------------------
#   Function definitions
#------------------------------------
def init():
    fname = 'words.txt'
    fhand = open(fname)
    for line in fhand:
        words = line.split()
        if not len(words) : continue    #avoid empty lines
        line_traverser(words)

def line_traverser(wds):
    for word in wds:
        # removes all type of marks that might be found at the end of the word
        temp_word = re.sub(r'\W','',word.lower()[len(word)-1])
        if temp_word != word[len(word)-1]: word = word[:len(word)-1]

        # This is for:
        #   - when the below step clean an only-mark-symbol word and now the word has cero length
        #   - when the word is numeric, and therefore it doesn't count like a word for the dictionary
        if not len(word) or word.isnumeric() : continue

        #when all the word are lower o upper(insensitive case)
        word_counter_dict[word] = word_counter_dict.get(word, 0) + 1

#------------------------------------
#   Main
#------------------------------------
word_counter_dict = dict()
init()
print(word_counter_dict)