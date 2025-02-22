#Q1 Wep to check a number entered by user is odd or even 
print("Check the number is odd or even")
num=int(input("Please enter a number :"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")
print("Program End")
print("------------------------------------------------------------------")


#Q2 WEp to find the greatest of 3 numbers entered by the user 
print("Find the greatest of 3 numbers")
num1=int(input("Please enter first number :"))
num2=int(input("Please enter second number :"))
num3=int(input("Please enter third number :"))
if(num1>num2 and num1>num3):
    print("The greatest number is The first number which is = ",num1)
elif(num2>num1 and num2>num3):
    print("The greatest number is The second number which is = ",num2)
else:
    print("The greatest number is The third number which is = ",num3)
print("Program End")
print("------------------------------------------------------------------")

#Q3 Wep to check if a number is a multiple of 7 or not
print("Check the number is multiple of 7 or not")
n=int(input("Please enter a number :"))
if(n%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")
print("Program End")
print("------------------------------------------------------------------")


#Q4 Wep to check if a number is a multiple of 3 and 7 
print("Check the number is multiple of 3 and 7 or not")
n1=int(input("Please enter a number :"))
if(n1%3==0 and n1%7==0):
    print("The number is multiple of 3 and 7")
else:
    print("The number is not multiple of 3 and 7")
print("Program End")
print("------------------------------------------------------------------")
#Q5 Create a tabel of 8 multiplication
print("Table of 8")
for i in range(1,11):
    print("8 * ",i," = ",8*i)
print("Program End")
print("------------------------------------------------------------------")
#Q6 Wep to check if a number is positive or negative
print("Check the number is positive or negative")    
num3=int(input("Please enter a number :"))
if(num3>0):
    print("The number is positive")
else:
    print("The number is negative")