# write a recursive python function to calculate sum  of first N natural numbers
def sumOfN(num):
    if num==1:
        return 1
    return num+sumOfN(num-1)
num=int(input("enter a number"))
result=sumOfN(num)

print(f"sum of first {num} natural number is {result}")