info={
    "Name":"Tasnia ",
    "ID":221-35-982,
    "Department":"SWE",
    "fev_sub":["AI","ML","MIS"],
    "code_tuple":(5,3,6,2,1),
    "University":"DIU",
    "Semester":8,
    "Age":21,
    "Blood Group":"O+",
    "is_Adult":True

}
null_dictionary={

}
print(null_dictionary)

print(info)
print(info["Blood Group"])
print(info["Name"])
print(type(info))
print(len(info))
fev=len(info["fev_sub"])
print(fev)
print(info["fev_sub"])
#dictionary  is mutable
info["Age"]=22
print(info) 
info["Name"]="Masuduzzaman Niloy"
print(info)
info["fev_sub"].append("C#")
print(info)
info["fev_sub"].remove("AI")
print(info)
info.pop("Blood Group")
print(info)
info.popitem()
print(info)
del info["University"]
print(info)


