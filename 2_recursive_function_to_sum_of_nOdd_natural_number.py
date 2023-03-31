# write a recursive  python function fo   calculate sum    of first N odd  natural numbers
def sumOfodd(num):
    if  num==1:
        return 1
    return ((num*2)-1)+sumOfodd(num-1)

r=sumOfodd(3)
print(r)