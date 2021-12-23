def square(a):
    return a**2

n = int(input())
a = list(map(int, input().rstrip().split()))
x = list(map(square, a))

print(*x)
print(str(x)[1:-1])
print(' '.join(map(str, x)))
for i in x:
    print(i, end= " ")
