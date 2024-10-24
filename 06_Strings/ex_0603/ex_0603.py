# -----------------------------------
# Imports and Global Variables
# -----------------------------------

# -----------------------------------
# Function Definitions
# -----------------------------------
def count(s,letter):
    amount_of_letter = 0
    for i in s:
        if i == letter:
            amount_of_letter += 1
    print('Total of letter "', letter,'" in', s , 'is', amount_of_letter)

def user_letter_recursive_function():
    user_entry_letter = input('Write a letter: ')
    if user_entry_letter == 'done':
        quit()
    elif len(user_entry_letter) == 1:
        count(user_entry_string,user_entry_letter)
    else:
        print("Please enter only one letter")
        user_letter_recursive_function()

# -----------------------------------
# Main Execution Code
# -----------------------------------
while True:
    user_entry_string = input('Write a sentence or "done" to end: ')
    if user_entry_string == 'done':
        break
    user_letter_recursive_function()
