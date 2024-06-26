c=input("Enter number: ")
for i in range(2, c):
    if (c%i == 0):
        continue
    else:
        print(i)
