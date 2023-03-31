# write a recursive python function to  print octal of a given decimal number
def octal(num):
    if num==0:
        return 0
    else:
        return num%8 + 10* octal(num//8)
num=int(input("enter the number"))
res=octal(num)
print(res)

'''

print("--------2nd way to find the ocatal of given decimal number-----------")
def find(num):
    if num!=0:
        find(num//8)
        print(num%8)
num=int(input("enter a number"))
find(num)

'''