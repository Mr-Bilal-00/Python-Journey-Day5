a=int(input("Enter No : "))
b=int(input("Enter No : "))
c=int(input("Enter No : "))

if(a>b):
    if(a>c):
        print("Greatest No is ",a)
    else:
        print("Greatest No is ",c)
elif(b>c):
    print("Greatest No is ",b)
else:
    print("Greatest No is ",c)

