count = 0
total = 0
number_int = None
compute = [0, 0, 0]

def compute_aveg(n):
    global count
    global total
    total = total + n
    # print(total)
    count = count + 1
    # print(count)
    return [total, count, float(total/count)]

while True:
    number = input('Enter an integer number or "done" to finish: ')
    if number == 'done':
        break
    try:
        number_int = int(number)
    except:
        print('Invalid input')
        continue
    compute = compute_aveg(number_int)

print(compute[0], compute[1], compute[2])


