lst = [2]
n = int(input("Enter a number: "))
for i in range(3,n+1):
    if i%2 != 0:
        lst.append(i)

print(lst)