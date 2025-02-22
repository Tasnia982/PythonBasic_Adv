#set in python and set element is immutable so we don't use here dictionary and list 
#cz dictionary and list is mutable 
# set is mutable but set elements is immutable
#set is unordered collection of unique elements
collection={"TAsnia","Tasnia","Hello",5,4,2,7,8,12,18}
collection.add("Tonima")
print(collection)
print(type(collection))
print(len(collection))
print(collection)

dic={}
print(type(dic))

PySet=set()
print(type(PySet))

print("-------------------Set Method ------------------------------")
#set add method
print("-----------Add Method-----------------")
collection.add("Niloy")
#collection.add("TAsnia","Tawabur","Utshab")(error asbe cz 1 element ar basi dawa jai na)
print(collection)

# # # set remove method
print("-----------Remove Method-----------------")
collection.remove("Hello")
print(collection)

# # #set clear method
print("-----------Clear Method-----------------")
collection.clear()
print(collection)
collection.add("Tonima")
collection.add("Tasnia")
collection.add("Hello")
print(collection)

# # #set pop method 
print("-----------------------pop method-------------------------")
collection.pop()
print(collection)
#union
print("-----------------------Union Method-------------------------")
set1={3,2,3,2,4,5,67,54,3}
set2={5,4,3,5,3,5,2,776,5,654,45}
print(set1.union(set2))



#intersection
print("-----------------------Intersection Method-------------------------")
print(set1.intersection(set2))



