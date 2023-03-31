# write  a recursive python function to calculate  sum  of  cubes of first N natural number
def sumOfCubes(num):
    if num==1:
        return 1
    return num**3 + sumOfCubes(num-1)
num=int(input("enter  a number"))
res=sumOfCubes(num)
print(res)