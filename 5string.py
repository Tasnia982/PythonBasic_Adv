
str1="This is one type of string"

str2='This is another type of string'

str3="""This is a multiline string """

finalString="We use  str1 type of string"

str="This is a string.\n Use new line here using \\n . \n Using long space using \\t \t and using \\b for backspace. \b"
print(str)
print("--------------------------------------------------------------------------------------")

#string concatenation using + operator
str4=str1+str2
print(str4)
str5=str3+" "+finalString
print(str5)

print("--------------------------------------------------------------------------------------")
#string Length using len() function
print(str1)
print(len(str1))
print("--------------------------------------------------------------------------------------")
#string indexing
print(str1) 
print(str1[0])
print(str1[1])
print(str1[9])
print("--------------------------------------------------------------------------------------")
#string slicing
str6="This is a string using slicing opperation"
#slicing=str6=[starting index:ending index]
print(str6)
print(str6[0:4])
print(str6[3:7])
print(str6[8])
print(str6[15])
print(str6[:10])
print(str6[10:])
print(str6[:])
#Negative indexing
print(str6[-1])
print(str6[-5:-1])
print("--------------------------------------------------------------------------------------")
#string slicing with skip value
str7="This is a string using slicing with skip value"   
#slicing=str7=[starting index:ending index:skip value]
print(str7) 
print(str7[0:10:2])
print(str7[0:10:3])



