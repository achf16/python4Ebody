min_so_far = None
max_so_far = None

min_max = [ 0 , 0 ]

def compute_min_max(n):
    global min_so_far
    global max_so_far

    if min_so_far is None or n < min_so_far:
        min_so_far = n
    if max_so_far is None or n > max_so_far:
        max_so_far = n
    return min_so_far, max_so_far

while True:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        break

    try:
        number= float(user_input)
    except:
        print('Invalid input')
        continue

    min_max = compute_min_max(number)

print('Maximum is', int(min_max[1]))
print('Minimum is', int(min_max[0]))
