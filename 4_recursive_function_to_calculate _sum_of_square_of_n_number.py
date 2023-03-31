# write a  recursive  python function to calculate sum of  square of first  N natural numbers
def sumOfSquare(num):
    if num==1:
        return 1
    return (num**2)+sumOfSquare(num-1)
num=int(input("etner the number"))
res=sumOfSquare(num)
print(res)