# Description: This file contains the string functions in python.
#endWith("er.")
str="Hello ! this is a code"
print(str)  
print(str.endswith("code"))
print(str.endswith("ad"))
print("--------------------------------------------------------------------------------------")

#capitalize()
str1="hello ! Check this code"
sr2=str1.capitalize()
print(sr2)
print(str1)
print(str1.capitalize())

print("--------------------------------------------------------------------------------------")



#center()   
str2="Hello ! this is a code"
print(str2)
print(str2.center(50))
print(str2.center(50,"*"))
print("--------------------------------------------------------------------------------------")
#replace(old,new)
str3="Hello ! this is a code"
print(str3)
print(str3.replace("Hello","Hi"))
print(str3.replace("code","program"))
print("--------------------------------------------------------------------------------------")
#find()
str4="Hello ! this is a code"
print(str4)
print(str4.find("Hello"))
print(str4.find("this"))
print(str4.find("code"))
print("--------------------------------------------------------------------------------------")
#count()
str5="Hello ! this is a code"
print(str5)
print(str5.count("H"))
print(str5.count("this"))
print(str5.count("code"))
print("--------------------------------------------------------------------------------------")
#join()
str6="Hello ! this is a code"
print(str6)
print(" ".join(str6))
print(".".join(str6))
print("--------------------------------------------------------------------------------------")


