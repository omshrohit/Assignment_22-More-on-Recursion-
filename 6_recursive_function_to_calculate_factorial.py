# write a recursive python function to calculate factorial of a number.
def fect(num):
    if num==0:
        return 1
    return num*fect(num-1)
num=int(input("enter  a number"))
res=fect(num)
print(res)