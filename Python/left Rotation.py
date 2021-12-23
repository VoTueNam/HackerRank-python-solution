def rotateLeft(d, arr):
    last = []
    for i in range(len(arr),d,-1):
        last.insert(0,arr.pop())
    print(last)
    arr = last + arr
    return arr

arr = [1,2,3,4,5,6]
print(rotateLeft(2,arr))

