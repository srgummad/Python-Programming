largest = None
smallest = None
val=None
while True:
    num = raw_input('Enter a number :')
    try:     
        val=int(num)    
    except:
        print "Invalid input"
         
    if num == "done" : break
    if largest is None :
        largest=val
    if smallest is None :
        smallest=val
    if val>largest :
        largest=val
    if val<smallest :
        smallest=val 
print "Maximum is", largest
print "Minimum is", smallest