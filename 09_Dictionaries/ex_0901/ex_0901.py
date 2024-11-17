#------------------------------------
#   Global definitions and libraries
#------------------------------------
import re
from operator import length_hint


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
        temp_word = re.sub(r'\W+','',word.casefold()[len(word)-1])

        # This is for:
        #   - when the below step clean an only-mark-symbol word and now the word has cero length
        #   - when the word is numeric, and therefore it doesn't count like a word for the dictionary
        if not len(word) or word.isnumeric() : continue

        # if temp_word != word.casefold(): word = word[len(word) - 1]

        #when all the word are lower o upper(insensitive case)
        word_counter_dict[word] = word_counter_dict.get(word, 0) + 1

        # temp_word_counter_dict = dict()
        # if temp_word_counter_dict.get(temp_word, 0) :
        #     word_counter_dict[word] = word_counter_dict[word] + 1
        # else:
        #     word_counter_dict[word] = 1


#------------------------------------
#   Main
#------------------------------------
#TODO: set all the word in lower to compare and casefold for special characters
#TODO: I need a temp_Dict because it's necessary compare LowerToLower without losing the original word
word_counter_dict = dict()
init()
print(word_counter_dict)