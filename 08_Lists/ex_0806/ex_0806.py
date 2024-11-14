#-----------------------------------
#   Global definitions and Libraries
#-----------------------------------
number_list = list()
#-----------------------------------
#   Functions definitions
#-----------------------------------
def init():
    user_input = input("Enter a number or 'done' to finish: ")
    if user_input == 'done':
        print(f'Maximun: {max(number_list)}')
        print(f'Minimun: {min(number_list)}')
        quit()
    try:
        number = float(user_input)
    except:
        print("Please enter a number")
        return init()
    return number

def store_number(n):
    global number_list
    number_list.append(n)
#-----------------------------------
#   Main
#-----------------------------------
while True:
    store_number(init())
    # print(f'Maximun: {max(number_list)}')
    # print(f'Minimun: {min(number_list)}')