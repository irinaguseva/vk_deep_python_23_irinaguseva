from itertools import zip_longest

class CustomList(list):
    def __add__(self, other):

        lst_add = []
        for (a, b) in zip_longest(self, other, fillvalue=0):
            lst_add.append(a + b)

        return CustomList(lst_add)

    def __sub__(self, other):

        lst_sub = []
        for (a, b) in zip_longest(self, other, fillvalue=0):
            lst_sub.append(a - b)

        return CustomList(lst_sub)

    def __radd__(self, other):

        lst_radd = []
        for (a, b) in zip_longest(self, other, fillvalue=0):
            lst_radd.append(a + b)

        return CustomList(lst_radd)

    def __rsub__(self, other):

        lst_rsub = []
        for (a, b) in zip_longest(self, other, fillvalue=0):
            lst_rsub.append(b - a)

        return CustomList(lst_rsub)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)
    
    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"CustomList: [{', '.join(map(str, self))}], summa: {sum(self)}"