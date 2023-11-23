
arr = [4,2,76,10,7,1]
def smallest(arr):
    small = arr[0]
    for elem in arr:
        if small>elem:
            small=elem
    return small
print(smallest(arr))