#arthematic operations 
a=int(input("enter value a \n"))
b=int(input("enter value b\n"))
print(f"the addition of values is {a+b}")
print(f"the subraction of value is {a-b}, multiplication is {a*b},division is {a%b}, module is {a/b}")
print(f"the power is {a**b}")
#checking wheather the person can drive 2 or 3 wheeler vechile by using logical operators 
#and by conditional if else stmnts
age=int(input("enter age"))
if(age>=18) and (age<24):
 print("only two wheeler")
elif(age>=22 and age<=45):
 print("you are eligible for 2 wheeler")
else:
 print("you are eligible for 2 , 4, and 6 wheeler")
 #checking whheather is the vendor good or bad .. by comapring the total cost and the total money
 #by arthematic and logical operators and conditional statements
 apples=int(input())
bananas=int(input())
oranges=int(input())
total=int(input())
print(f"total is {total}")
cost=(apples*15)+(oranges*4)+(bananas*4)
print(f"cost is {cost}")
if cost<=total:
    print("good vendor")
else:
    print("he is a cheater")
