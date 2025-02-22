#recursion one kind of loop who call itself repetately . it's one kind of loop who call itself repetately . it's one kind of loop who call itself repetatel.

# print("---------Recursion use for print 5 to 1 -----------")
# def show(n):
#     if n==0 : #base case (decision jaikhana nai ja thambe kokhon )
#         return
#     print(n)
#     show(n-1)

# show(5)
# print("program end")


print("----------calculatr sum of first n natural number -----------")
def sum(n):
    if n==0 :
        return 0
    return sum(n-1)+n

  
  
print(sum(7))
