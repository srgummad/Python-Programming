name=raw_input("Enter File:")
if len(name) < 1: name="mbox-short.txt"
handle=open(name)
counts=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith("From ") : continue
    words=line.split()      
    counts[words[1]]=counts.get(words[1],0)+1
gnum=None
gsend=None
for a,b in counts.items():
    if gnum is None or b>gnum:
        gnum=b
        gsend=a
print gsend,gnum
    