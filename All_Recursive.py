def subsets(cur: str, n):

    if len(cur) == n:
        print(cur)
        return
    subsets(cur + '0', n)
    subsets(cur + '1', n)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def febo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return febo(n - 1) + febo(n - 2)


def pick_or_leave(i):
    if i == len(str):
        print(result)
        return
    pick_or_leave(i + 1)

    result.append(str[i])
    pick_or_leave(i + 1)
    result.pop()

def fn(st):
    dct = {}
    for i in range(len(st)):
        if st[i] in dct:
            dct[st[i]].append(i)
        else:
            dct[st[i]] = []
            dct[st[i]].append(i)
    
    sub_arrays = []
    sub_arrays_2 = []
    for lst in dct.values():
        sub_arrays.append(st[min(lst):max(lst) + 1])
        sub_arrays_2.append(st[0:min(lst)] + st[max(lst) + 1: len(st)])
    print(dct)
    arr = [-1] * len(st)
    print(arr)

    
    print(arr)
    return dct


def knap(i, remain):
    if i == len(w):
        return 0
    if w[i] > remain:
        return knap(i + 1, remain)

    return max(knap(i + 1, remain), knap(i + 1, remain - w[i]) + v[i])

w = [10, 4, 6, 5, 1]
v = [10, 15, 2, 8, 2]
lim = 21

print(knap(1, 11))


print(febo(4))