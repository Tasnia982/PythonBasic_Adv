#list and tuple are similar but the main difference is that list is mutable and tuple is immutable
#Tuple in Python
print("Tuple in Python")
tup=(1,2,3,4,5,6,7,8,9)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[3:8])
print(tup.index(2))
print(tup.index(7))
print(tup.count(5))
print(tup[-1])
tup2=("Tasnia","Niloy","Utshab","Sakib",8,5,9,7)
print(tup2)
#practice Problem
#wep to ask the user to enter name of their 3 favorite movies and store them in a  list 
print("Practice Problem Q-1 " )
movie=["3idiots","Business Purpose","Quin  of teirs "]
print(movie)
print(type(movie))
print(len(movie))

#TAking input from user
print("Taking input from user")
mov=[]
mov.append(input("Enter your 1st fav movie: "))
mov.append(input("Enter your 2nd fav movie: "))
mov.append(input("Enter your 3rd fav movie: "))
print(mov)

 

 #Q-2 : wep to check if a list contains a palindrome of elements 
#print("Practice Problem Q-2 " )
palindrome1=["madam","level","radar","civic","deified"]
palindrome2=[2,43,3,4]
copy_palindrome1=palindrome1.copy()
copy_palindrome1.reverse()
if copy_palindrome1==palindrome1:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
print(palindrome1)
print(type(palindrome1))
print(len(palindrome1))
print(palindrome1[0])
print(palindrome1)


print("-----------OR----------------")
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
print(list1)


#wer to count the numberof students get "A" grade in this tuple 
#tuple=("c","d","a","a","b,"b","a")

print("Practice Problem Q-3 " )
tuple=("c","d","a","a","b","b","a")
print(tuple)
print(tuple.count("a"))
print(tuple)

#store the above values in a list and sort them from "a"to "d"

print("Sort the given Tuple ")
print(type(tuple))
t=list(tuple)
print(t)
t.sort()
print(t)
