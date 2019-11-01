'''Print fibonachi series and sum of that series'''
s = int(input("Enter you number here: "))
l = [0,1]
def func1(s):
    a = 0
    b = 1
    sum = 0
    while sum < s:
        sum = a + b
        a,b = b,sum
        if sum < s:
            l.append(sum)
    return(l)

k = func1(s)
print("Your list looks like this:",k)
print("Sum of your list is this:",sum(k))

