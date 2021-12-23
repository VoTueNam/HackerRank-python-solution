def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum +=i
    return sum


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)