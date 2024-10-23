# Rewrite the exercise 3.2, this time using a function that takes two parameter(hours, rate)
# To have a returned value to the main functions is a requirement of the exercise, but it's not necessary

def computepay(hours, rate):
    if worked_hours <= 40:
        return worked_hours * rate_per_hours
    else:
        return worked_hours * rate_per_hours + (worked_hours - 40) * rate_per_hours * 0.5

try:
    worked_hours = float(input('Enter Hours: '))
except:
    print('Error, please enter a numeric input')
    quit()

try:
    rate_per_hours = float(input('Enter Rate: '))
except:
    print('Error, please enter a numeric input')
    quit()

print('Pay',computepay(worked_hours, rate_per_hours))