# №1 на базе списка два стека длинной n

list_stack = [0 for i in range(n*2)]
ind1 = 0
ind2 = n
new_element = 1
num_stack = 1  or 2

def stack_push(lst, n, ind1, ind2, new, num_stack):
    if num_stack == 1:
        lst = lst[:(n/2)]
        if ind1 == n:
            print("full")
        else:
            lst[ind1] = new
            ind1 += 1
            return (lst, ind1)
    elif num_stack == 2:
        lst = lst[(n/2):]
        if ind2 == n*2:
            print("full")
        else:
            lst[ind2] = new
            ind2 += 1
            return (lst, ind2)

def stack_pop(ind1, ind2, num_stack):
    if num_stack == 1:
        if ind1 == 0:
            print("empty")
        else:
            ind1 -= 1
            return (ind1)

    elif num_stack == 2:
        if ind2 == n:
            print("empty")
        else:
            ind2 -= 1
            return (ind1)

def IsEmpty(ind1, ind2, num_stack):
    if num_stack == 1:
        if ind1 == 0:
            print("empty")
        else:
            print("no_empty")

    if num_stack == 2:
        if ind2 == n:
            print("empty")
        else:
            print("no_empty")




# №2 очередь на базе двух стеков
class Stack:
    def __init__(self, n):
        self.stack_push = [0 for i in range(n)]
        self.ind_push = 0

        self.stack_pop = [0 for i in range(n)]
        self.ind_pop = 0

    def push(self, new):
        if self.ind_push != len(n):
            self.stack_push[self.ind_push] = new
            self.ind_push += 1
        else:
            print("full")

    def pop(self):
        if self.ind_pop == 0:
            if self.ind_push == 0:
                print("Empty")
            else:
                while self.ind_push != 0
                    self.stack_pop = self.stack_push[ind_push]
                    self.ind_push -=1
                    self.ind_pop += 1
                return pop(self)
        else:
            self.ind_pop -= 1


    def size(self):
        return(self.ind_push)

    def IsEmpty(self):
        if self.ind_push == 0:
            print("empty")
        else:
            print("no_empty")

    def top(self):
        if self.ind == 0:
            print("Empty")
        else:
            return(self.stack_push[self.ind_push])

# функции push, size, isEmpty, top - сложность О(1) так как она не зависит от длины n
# фунция pop: при заполненном stack_push - сложность фунции pop - О(n)














