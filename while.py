"""
x=1
while x<7:
    print(x)
    x+=1 #or x=x+1
print("Completed")
"""

"""
x=1
while x<7:
    print(x)
    if x==3:
        break
    x+=1 #or x=x+1
"""


x=1
while x<7:
    x=x+1
    if x==3:
        continue
    print(x)
else:
    print("x is no longer less than 7!")
#break statement ke sath else statemant use nh kar sakte
