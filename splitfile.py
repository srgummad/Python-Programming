fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    line=line.rstrip()
    templst=line.split()
    for w in templst :
        if not w in lst :
            lst.append(w)
lst.sort()
print lst
    