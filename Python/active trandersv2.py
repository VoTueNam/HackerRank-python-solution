
import time
# def mostActive(customers):
#     customers.sort()
#     b = []
#     a = list(set(customers))
#     soluong = 0
#     for i in a:
#         for cus in range(soluong,len(customers)):
#             if i == customers[cus]:
#                 soluong += 1
#         if soluong/len(customers) >= 0.05:
#             print(soluong/len(customers))
#             b.append(i)
#         soluong = 0
#     return b

def most2(customers):
    store = dict()
    res = []
    for i in customers:
        if i in store:
            store[i] +=1
        else:
            store[i] = 1
    print(store)
    for i in store.items():
        if i[1]/len(customers) >= 0.05:
            res.append(i[0])
    return res


if __name__ == '__main__':
    customers = ["Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Beta"]
    result = most2(customers)
    print(result)
    