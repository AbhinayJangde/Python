def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-2) + fibo(n-1)

lst =[]
n = int(input("Enter how many fibonacci numbers you want?: "))
for i in range(0,n+1):
    lst.append(fibo(i))

print(lst)