name=raw_input("Enter the file name:")
if len(name)<1: name="mbox-short.txt"
handle=open(name)
l=list()
d=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    temp=line.split()
    temp2=temp[5]
    temp3=temp2.split(":")
    d[temp3[0]]=d.get(temp[0],0)+1
for k,v in sorted(d.items()):
    print k,v
    