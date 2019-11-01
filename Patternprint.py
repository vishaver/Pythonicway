'''Print starts here based on true and false'''
r = int(input("Enter the number: "))
k = str(input("Enter True or False: "))
if k == "True":
    m = 1
    for j in range(r):
        print("*" * m)
        m = m + 1
elif k == "False":
    for j in range(r):
        print("*"*r)
        r = r - 1

