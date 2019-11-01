'''Calculate the factorial of number'''
def func1(num):
    print("You are in normal function")
    k=1
    for j in range(num):
        k = k * (j + 1)
    return(k)

s = int(input("Enter your number here: "))
print(func1(s))

'''Recursive approach'''

def func2(num):
    print("You are in recursive function")
    if num == 1:
        return 1
    else:
        return num * func2(num - 1)

s = int(input("Enter your number here: "))
print(func2(s))

