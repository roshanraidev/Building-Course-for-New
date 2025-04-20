# this loop is used to iterate until the initial condition becomes false

x = 0

while x<10:
    print(f'the value of x is {x}')
    x+=1
else:
    print("The loop is broken")


# we can use break,continue,pass statements to provide more functionality to the loops
# break - breaks out of the current closest enclosing loop
# continue - goes to the top of the current closest enclosing loop
# pass - does nothing at all

x ={1,2,3}

for i in x:
    pass

print("The pass keyword is used to get out of the loop , if we are not sure what to do with the loop")

#----------------------------------------------------------------------------------------------------------
mystring ='sammy'

for l in mystring:
    if l == 'm':
        continue   # goes to the top of loop , does not print m and moves on to next iteration
    print(l)

#----------------------------------------------------------------------------------------------------------

x =0

while x<5:
    if x == 2:
        break    # breaks out of the loop and does not continue
    print(x)
    x+=1




