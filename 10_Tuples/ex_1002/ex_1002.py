#--------------------------------------
#   Global definitions and libraries
#--------------------------------------
hour_histogram = dict()
#--------------------------------------
#   Function definitions
#--------------------------------------
def init():
    while True:
        fname = input('Enter file name or "done" to quit: ')
        if fname == 'done': quit()
        elif not len(fname): fname = "mbox-short.txt"
        try:
            fhand = open(fname)
            return fhand
        except:
            print("Failed to open", fname, ". File does not exist.")

def lines_traverser(fh):
    for line in fh:
        if not line.startswith('From '): continue
        dictionary_builder(line.split()[-2].split(":")[0])

def dictionary_builder(key):
    hour_histogram[key] = hour_histogram.get(key, 0) + 1

def sort_hours(d):
    sorted_d = sorted(d.items())
    for i in range(len(sorted_d)):
        hour_histogram[sorted_d[i][0]] = hour_histogram.pop(sorted_d[i][0])

#--------------------------------------
#   Main
#--------------------------------------
while True:
    lines_traverser(init())
    sort_hours(hour_histogram)
    for key,value in hour_histogram.items():
        print(f"{key} {value}")