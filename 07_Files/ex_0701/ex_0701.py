fmbox = open('mbox-short.txt')
for line in fmbox:
    fmbox_stripped = line.rstrip()
    print(fmbox_stripped.upper())
fmbox.close()
