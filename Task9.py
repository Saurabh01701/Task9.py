print("Saurabh's Calculator")
print("press 1. for adition")
print("press 2. for subtraction")
print("press 3. for multiplication")
print("press 4. for division")
x=int(input("Enter your choice:"))
a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
match x:

  case 1:
    c=a+b
    print("addition of the numbers is:",c)      
  case 2:
    c=a-b
    print("subtraction of the numbers is:",c)
  case 3:
    c=a*b
    print("multiplication of the numbers is:",c)
  case 4:
    c=a/b
    print("division of the numbers is:",c)
  case 5:
    print("wrong choice")