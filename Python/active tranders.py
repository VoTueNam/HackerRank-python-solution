def mostActive(customers):
    customers.sort()
    b = []
    a = list(set(customers))
    for i in a:
        soluong = 0
        for cus in customers:
            if i == cus:
                soluong += 1
        if soluong/len(customers) >= 0.05:
            print(soluong/len(customers))
            b.append(i)
    return b


if __name__ == '__main__':

    customers = ["Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Beta"]
    result = mostActive(customers)
    print(result)