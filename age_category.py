age=int(input("Enter you'r age : "))
if(age<13):
    print("Child")
elif(age>=13 or age<=19):
    print("TEEN")
elif(age>=20 or age<=59):
    print("ADULT")
elif(age>=60):
    print("senior")
print("Thanks!")