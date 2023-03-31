# write  a recursive python  function to print binary of a  given dicimal number
def binary(num):
    if num==0:
        return 0
    else:
        return num%2 + 10* binary(num//2)
        
    
num=int(input("enter a number"))
res=binary(num)
print(res)
