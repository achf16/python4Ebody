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

if worked_hours <=  40:
    print('Pay:', worked_hours * rate_per_hours)
else:
    print('Pay:', worked_hours * rate_per_hours + (worked_hours-40)*rate_per_hours*0.5)