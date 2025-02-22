#while loop 
print("----------Q-1: print numbers from 1 to 100 -------------------")
print("----------------------------While loop------------------------------")
i = 1
while(i<=100):
    print(i)
    i +=1
else:
    print("Program End ! ") 

print("--------------Q2 : print number from 100 to 1--------------------")       
j=100
while j>=1 :
    print(j)
    j -=1
else:
    print("Program end ")


print("-------Q3=print the multiplication table of a number n -------------")
n=int(input("Please enter the number you want to see the multiplication table of:"))
i=1
while i<=10 :
    print(n ,"*" ,i ,"=", n*i)
    i +=1
else:
    print("Program end !")    

print("-----------------for loop --------------------")
print("-----------Q4 = Print the elements of the following list using a loop  ----------")
numbers = [1, 2, 3, 4, 5, 6,9,89,87,90]
for num in numbers :
         print(num)
else:
     print("Program ended !")         

print("-------------------OR----------------------")
i=0
while i<len(numbers) :
     print(numbers[i])
     i +=1

else:
     print("Program End!")



print("------------------Q5 = search a number x in this tuple using loop ------------------")
tuple1=(1,2,3,4,5,6,7,8,9)
x=int(input("Please enter the number you want to search in the tuple:"))
for num in tuple1 :
     if num==x:
          print(x,"is found in the tuple")
          break
else:
    print(x,"is not found in the tuple")
          
          

