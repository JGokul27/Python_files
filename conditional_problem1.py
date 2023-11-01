# take user input
age = int(input("Please type the age:"))

#check condition
if age < 12:
    print("Child")
elif (age > 14 and age < 19):
    print("teenager")
elif (age > 40 and age < 60):
    print("old")
elif (age > 20 and age < 40):
    print("young")