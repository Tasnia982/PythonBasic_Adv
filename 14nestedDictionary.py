#Nested Dictionary 
Student={
    "Name":input("Please enter your name:"),
    "Age":int(input("Please enter your age:")),
    "sub_num":{
        "AI":79,
        "ML":93,
        "DL":87
    },
    "CGPA":3.95 
}
print(Student)
print(Student["sub_num"])
print(Student["sub_num"]["ML"])
Student["ML"]=49
print(Student["sub_num"])
print("-----------------------------------------------------------")



#dictionary Method 
#student.keys(),student.values(),student.items(),student.get("key"),student.update(newDict)::: Here student mean dictionary name 



print("---------dictionary keys() method----------")
print(Student.keys())
print(list(Student.keys()))
print(str(Student.keys()))
print(type(Student))
print(tuple(Student.keys()))
print(type(Student))
print("-----------------Lenth Method----------------------")
print(len(Student))
print(type(len(Student)))
print("------------------Values method---------------------")
print(Student.values())
print(list(Student.values()))
print(type(Student.values()))
print(len(Student["sub_num"]))
print(type(Student["sub_num"]))
print("-------------------------------")

print("-----------------items method-------------------------")
print(Student.items())
print(list(Student.items()))
print(type(Student.items()))


#dictionary  get method use for if any key is not present in dictionary then it will return None rether then giving error

print("----------------get method-------------------------")
print(Student.get("Name"))
print(Student.get("Age"))
print(Student.get("Nam"))
print(Student.get("sub_num3"))
print(type(Student.get("Nam")))



#update Method 

print("------------------Update Method -------------------------")
print(Student)
Student.update({"Name":"Rahul","Age":20,"sub_num":5})
print(Student)
print(type(Student))

