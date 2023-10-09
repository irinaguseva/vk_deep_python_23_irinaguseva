class CustomList(list):
    def __add__(self, other):
        if not isinstance(other, list):
            raise TypeError()
        rng = min(len(self), len(other))
        lst_add = [self[i] + other[i] for i in range(rng)]
        if len(self) > len(other):
            for j in range(len(other), len(self)):
                lst_add.append(self[j])
        else:
            for k in range(len(self), len(other)):
                lst_add.append(other[k])
        return CustomList(lst_add)

    def __sub__(self, other):
        if not isinstance(other, list):
            raise TypeError()
        rng = min(len(self), len(other))
        lst_add = [self[i] - other[i] for i in range(rng)]
        if len(self) > len(other):
            for j in range(len(other), len(self)):
                lst_add.append(self[j])
        else:
            for k in range(len(self), len(other)):
                lst_add.append(-other[k])
        return CustomList(lst_add)

    def __radd__(self, other):
        if not isinstance(other, list):
            raise TypeError()
        rng = min(len(self), len(other))
        lst_radd = [self[i] + other[i] for i in range(rng)]
        if len(self) > len(other):
            for j in range(len(other), len(self)):
                lst_radd.append(self[j])
        else:
            for k in range(len(self), len(other)):
                lst_radd.append(other[k])
        return CustomList(lst_radd)

    def __rsub__(self, other):
        if not isinstance(other, list):
            raise TypeError()
        rng = min(len(self), len(other))
        lst_add = [other[i] - self[i] for i in range(rng)]
        if len(self) > len(other):
            for j in range(len(other), len(self)):
                lst_add.append(-self[j])
        else:
            for k in range(len(self), len(other)):
                lst_add.append(other[k])
        return CustomList(lst_add)

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