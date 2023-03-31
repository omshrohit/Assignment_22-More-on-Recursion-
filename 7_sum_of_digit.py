# write  a recursive  python function to   calculate the sum of the digits of a given number
def sumOfdigits(num):
    if num==0:
        return   0
    return num%10 + sumOfdigits(num//10)
num=int(input("enter the number"))
res=sumOfdigits(num)
print(res)
