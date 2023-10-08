from collections import UserList
from itertools import zip_longest


class CustomList(UserList):
    def __add__(self, other):
        if isinstance(other, CustomList):
            other = other.data
        elif not isinstance(other, list):
            raise TypeError("Сложение невозможно")

        if other is None:
            return CustomList(self.data.copy())
        lst_add = []
        for (a, b) in zip_longest(self.data, other, fillvalue=0):
            lst_add.append(a + b)
        return CustomList(lst_add)

    def __radd__(self, other):
        try:
            return self + other
        except TypeError as err:
            raise TypeError("Сложение невозможно") from err

    def __sub__(self, other):
        if isinstance(other, CustomList):
            other = other.data
        elif not isinstance(other, list):
            raise TypeError("Вычитание невозможно")

        if other is None:
            return CustomList(self.data.copy())
        lst_sub = []
        for a, b in zip_longest(self.data, other, fillvalue=0):
            lst_sub.append(a - b)
        return CustomList(lst_sub)

    def __rsub__(self, other):
        if isinstance(other, CustomList):
            other = other.data
        elif not isinstance(other, list):
            raise TypeError("Вычитание невозможно")
        if not other:
            return CustomList([x * (-1) for x in self.data])
        lst_rsub = []
        for (a, b) in zip_longest(other, self.data, fillvalue=0):
            lst_rsub.append(a - b)
        return CustomList(lst_rsub)

    def __lt__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) < sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __le__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) <= sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __eq__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) == sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __ne__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) != sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __gt__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) > sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __ge__(self, other):
        if issubclass(type(other), CustomList):
            return sum(self.data) >= sum(other.data)
        raise TypeError("Операция сравнения не может быть выполнена")

    def __str__(self):
        return f"CustomList({self.data}, sum = {sum(self.data)})"
