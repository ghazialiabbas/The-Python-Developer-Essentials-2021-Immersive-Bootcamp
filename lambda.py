#x= lambda i:i+11
#print (x(5))
#x= lambda i,y,z :i+y+z
#print (x(5,3,2))
def new(i):
    return lambda x: x*i
double =new(2)
triple= new(3)
print (double(5))
print (triple(5))