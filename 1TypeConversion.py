#input from user
name=input("Enter your name please=")
print("Hello",name)
print(type(name))

#input function always return string.so if we want any spacific type we have to convert it.
number=input("Enter your number=")
print(type(number))

number=int(input("Enter your number="))
print(type(number))



#type convertion 
a=4
b=3.5
print(a+b)#4.0+3.5=7.5
print(a*b)#4.0*3.5=14.0
#python will automatically convert the integer to float


#type custing
print(int(b))#3
print(float(a))#4.0
c=int("10")
SUM=c+a
print(SUM)#10+4=14
