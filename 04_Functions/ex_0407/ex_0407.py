# rewrite the exercise 4.7, this time using a function named "computegrade" that takes an score
# argument and return the corresponding grade as a string

def computegrade(score):
    if 1 > score_number > 0:
        if score_number >= 0.9:
            return "A"
        elif score_number >= 0.8:
            return "B"
        elif score_number >= 0.7:
            return "C"
        elif score_number >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Bad score"

try:
    score_number=float(input("Enter score: "))
except:
    print('Bad score')
    quit()

print(computegrade(score_number))
