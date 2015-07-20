inp=raw_input()
lst=inp.split()
a=int(lst[0])
b=int(lst[1])
n=int(lst[2])
fiblst=list()
def fib(m,a,b) :
    if m==0 :
        fiblst.append(a)
        return a
    elif m==1 :
        fiblst.append(b)
        return b
    else :
        return (pow(fib(m-1,a,b),2))+fib(m-2,a,b)
print fib(n-1,a,b)