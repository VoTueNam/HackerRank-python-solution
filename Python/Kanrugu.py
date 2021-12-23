def kangaroo(x1, v1, x2, v2):
    i = 0
    if x1==x2:
        return "YES"
    while True:
        i +=1
        if (v1 > v2 and x1 + v1*i > x2 + v2*i) or (v1 < v2 and x1 + v1*i < x2 + v2*i)or (v2 == v1 and x2 != x1):
            return "NO"
        if x1 + v1*i == x2 + v2*i:
            return "YES"

print(kangaroo(0,3,4,2))