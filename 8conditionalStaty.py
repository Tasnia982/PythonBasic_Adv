#if-else condition (normally use true or false related operation)

age=20
if(age>=18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")    

    print("-----------------------------------------------")

#use elif condition

light=input("Traffic Controller Please assign the light color : ")
if(light=="red" or light=="RED" or light=="Red"):
    print("Stop the vehicle")
elif(light=="yellow" or light=="YELLOW" or light=="Yellow"):
        print("Get ready to move")
elif(light=="green" or light=="GREEN" or light=="Green"):
        print("Move the vehicle")
else:
        print("Invalid color")
        
print("-----------------------------------------------")

num=input("Please enter your number : ")
#Just see the working process of if condition reather than elif condition
if(int(num)>=40):
    print("You pass the exam")
if(int(num)>=70):
    print('You get "A "grade')
if(int(num)>=80):
    print('You get "A+" grade')
else:
    print("You fail the exam")
print("Program End")
print("-----------------------------------------------")
#Marking in proper way 
print("CGPA Calculation")
mark=int(input("Please enter Student Number :"))
if(mark>=40 and mark<=49):
    print("You get D grade")
elif(mark>=50 and mark<=59):
    print("You get C grade")
elif(mark>=60 and mark<=69):
    print("You get B grade")
elif(mark>=70 and mark<=79):
    print("You get A grade")
elif(mark>=80 and mark<=100):
    print("You get A+ grade")
else:
    print("You fail the exam")
print("Program End")
print("------------------------------------------------------------------")
#Nested if else condition
print("Bonus Calculation")
salary=int(input("Please enter your salary : "))
if(salary>=10000):
    if(salary>=20000):
        print("You get 10% bonus")
    else:
        print("You get 5% bonus")
else:
    print("You get 2% bonus")   
print("Program End")
print("------------------------------------------------------------------")            


