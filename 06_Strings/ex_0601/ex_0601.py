while True:
    s = input("Write a word or sentence( 'done' to finish): ")
    if s == 'done':
        break

    print('---WHILE: BACKWARDS TRAVERSAL---')
    counter = 1
    while counter <= len(s):
        print(s[len(s)- counter])
        counter += 1

    print('')   # new line
    print('---FOR: BACKWARDS TRAVERSAL---')
    for i in range(-1, -len(s)-1,-1):
        print(s[i])