#1
d = [1, 5, 6, 11, 12]
f = 55

def find_gene(lst, pos):
    s = 1
    for i in lst:
        if s != len(lst):
            if i < pos < lst[s]:
                r = (lst[s] + i)/2
                if pos > r:
                    print(lst[s])
                else:
                    print(i)
        s += 1
    if pos > lst[len(lst)-1]:
        print(lst[len(lst)-1])
    elif pos < lst[0]:
        print(lst[0])
    elif lst.count(pos) == 1:
        for i in lst:
            if i == pos:
                print(i)
find_gene(d, f)

#3
f = [5,6,8,9,1,2,3,4,5,6,1,2]

def sum_p(lst):
    tmp = 0
    index = 0
    for i in lst:
        tmp += i
        lst[index] = tmp
        index += 1
    return lst
sum_p(f)

#4
g = [1,1,2,2,1,1,2,2,2,2,1,2,1,1,1]
f =[1,5,6,4,4,4,4,4,8,5,5,5,5]

def find(a):
    f = a[0]
    count = 1
    for i in a[1: len(a)]:
        if f == i:
            count += 1
        else:
            count -= 1
            if count == (-1):
                f = i
                count = 1
    if (len(a)/2) < a.count(f):
        return f
    else:
        return None
find(g)
# очевидно, что алгоритм по-прежнему работает за О(n), так как долнительный if проходится еще только один раз по массиву

