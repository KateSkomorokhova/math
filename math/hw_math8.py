# №1 бинарный поиск числа в массиве
a = [5,8,8,8,9]
b = 8


left_ind = 0
right_ind = int(len(a) - 1)

if a == []:
    print("-1")
elif len(a) == 1:
    if a[0] == b:
        print(0)
    else:
        print("-1")
elif a[0] == b:
    print(0)
elif b > a[right_ind] or b < a[left_ind]:
    print("-1")
elif a[left_ind] < b <= a[right_ind]:
    while left_ind < right_ind - 1:
        middle = int((left_ind + right_ind) / 2)
        if a[middle] < b:
            left_ind = middle
        else:
            right_ind = middle

    if a[right_ind] == b:
        print(right_ind)

    else:
        print('-1')
# Сложность бинарного поиска O(log2n) т.к. количество операций уменьшается вдвое с увеличением n





# №2 a+b = x

# 1- сортировка списка
def merge(a,b):
    c = [0 for x in range(len(a) + len(b))]
    indexA = 0
    indexB = 0
    while indexA != len(a) and indexB != len(b):
        if a[indexA] < b[indexB]:
            c[indexA + indexB] = a[indexA]
            indexA += 1
            continue
        else:
            c[indexA + indexB] = b[indexB]
            indexB += 1
            continue

    while indexA != len(a):
        c[indexA + indexB] = a[indexA]
        indexA += 1
    while indexB != len(b):
        c[indexA + indexB] = b[indexB]
        indexB += 1
    print(c)

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    lst[:int(len(lst)/2)] = merge_sort(lst[:int(len(lst)/2)])
    lst[int(len(lst)/2):] = merge_sort(lst[int(len(lst)/2):])
    lst = merge(lst[:int(len(lst)/2)], lst[int(len(lst)/2):])
    return lst
merge_sort(a)

# 2 - поиск элемента х в списке S
def find(a,b):
    left_ind = 0
    right_ind = int(len(a) - 1)

    if len(a) < 3:
        print("no a and b")
    elif a[0] == b:
        print(0)
    elif b > a[right_ind] or b < a[left_ind]:
        print("no x in S")
    elif a[left_ind] < b <= a[right_ind]:
        while left_ind < right_ind - 1:
            middle = int((left_ind + right_ind) / 2)
            if a[middle] < b:
                left_ind = middle
            else:
                right_ind = middle

        if a[right_ind] == b:
            return right_ind

        else:
            print("no x in S")
R_ind = find(S,x)
# 3 поиск таких a и b, что x = a+b
S = S[:right_ind]
# далее можно складывать первые и последние элементы списка на предмет возможного равенства х
# но это не похоже на бинарный поиск




