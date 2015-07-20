v=int(raw_input())
n=int(raw_input())
strinp=raw_input()
lst=strinp.split()
intlst=list()
for l in lst :
    intlst.append(int(l))
print intlst.index(v)
