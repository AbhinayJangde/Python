lst = [2,90,"abhi",3.14,(1,3)]
int_lst = []
for i in lst:
    if type(i) == int:
        int_lst.append(i)

print(int_lst)