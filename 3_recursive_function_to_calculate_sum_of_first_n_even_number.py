# write a recursive python function to calculate sum of first N odd  natural numbers
def SumOfeven(num):
    if  num==1:
        return 2
    return (num*2) + SumOfeven(num-1)
result=SumOfeven(5)
print(result)