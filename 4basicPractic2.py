#Wap to input side of a square & print its area
side=float(input("Please enter the side of the square : "))
area=side*side
print("The area of the square is : ",area)
print("--------------------------------------------------------------------------------")

#wap to input 2 floating point numbers and print their average 
num1=float(input("Please enter first number : "))
num2=float(input("please enter second number :"))
average=(num1+num2)/2
print("The average of the two numbers is : ",average)   
print("--------------------------------------------------------------------------------")

# wap to input 2 numbers and swap them
num1=int(input("Please enter first number : "))
num2=int(input("Please enter second number : "))
print("The numbers before swapping are : ",num1,num2)
temp=num1
num1=num2
num2=temp
print("The numbers after swapping are : ",num1,num2)
print("--------------------------------------------------------------------------------")

# wap to input 2 numbers and swap them without using third variable
num1=int(input("Please enter first number : "))
num2=int(input("Please enter second number : "))
print("The numbers before swapping are : ",num1,num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("The numbers after swapping are : ",num1,num2)
print("--------------------------------------------------------------------------------")

# wap to input 2 numbers and print True if a is greater than b else False
num1=int(input("Please enter first number :"))
num2=int(input("Please enter secont number :"))
if(num1>num2):
    print("True.Number 1 is greater then number 2 ")
else:
    print("False.Number 2 is not greater then number 1")

print("--------------------------------------------------------------------------------")    