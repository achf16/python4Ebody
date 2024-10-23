try:
    score_number=float(input("Enter score: "))
except:
    print('Bad score')
    quit()

if 1 > score_number > 0:
    if score_number >= 0.9:
        print("A")
    elif score_number >= 0.8:
        print("B")
    elif score_number >= 0.7:
        print("C")
    elif score_number >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Bad score")
