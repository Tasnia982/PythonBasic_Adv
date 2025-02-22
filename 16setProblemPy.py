#store following work meanings in a python dictionary 
print("----------------------------problem-1------------------------")
dic={
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat":"a small animal "
}
print(sorted(dic))
print(type(dic))
print(dic)



#You are given a list of subject for students . Assume one classroom is required for 1 subject . 
#How many classrooms are needed by all students .
print("----------------------------problem-2------------------------")
set={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(set))


#enter of 3 subject from the user and store them in a dictionary.start with an empty dictionary and add one by one . 
#use subject name as key & marks as value.
print("----------------------------problem-3------------------------")
sub={

}
sub["AI"]=["79"]
sub["ML"]=["89"]
sub["Python"]=["85"]
x=int(input("Enter Average CGPA = "))
sub.update({"Avg_CGPA":x})
print(sub)


 


#Figer out a way to store 9 and 9.0 as separate values in the set. 
print("----------------------------problem-4------------------------")
set={9,"9.0"}
print(set)
print("------------------------OR------------------------")
val={
    ("float",9.0),("int",9)
}
print(val)
