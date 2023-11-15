import weakref
import time
from memory_profiler import profile

n = 50000

class BookVal:
    def __init__(self, val):
        self.val = val

class MyBookSimple:
    def __init__(self, idnumber, rating, price):
        self.idnumber = idnumber
        self.rating = rating
        self.price = price

simple_start_time = time.time()
simple_books_lst = []
for i in range(n):
    simple_book = MyBookSimple(BookVal(100001), BookVal(8), BookVal(1500))
    simple_books_lst.append(simple_book)
simple_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса с обычными атрибутами составляет {simple_finish_time - simple_start_time}.")

simple_start_time = time.time()
for i in range(n):
    simple_books_lst[i].idnumber.val = BookVal(0)
    simple_books_lst[i].rating.val = BookVal(0)
    simple_books_lst[i].price.val = BookVal(0)
simple_finish_time = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов с обычными атрибутами составляет {simple_finish_time - simple_start_time}.")

@profile
def simple_memory():
    simple_books_lst = []
    for i in range(n):
        simple_book = MyBookSimple(BookVal(100001), BookVal(8), BookVal(1500))
        simple_books_lst.append(simple_book)
    for i in range(n):
        simple_books_lst[i].idnumber.val = BookVal(1)
        simple_books_lst[i].rating.val = BookVal(1)
        simple_books_lst[i].price.val = BookVal(1)
simple_memory()

class MyBookSlots:
    __slots__ = ['idnumber', 'rating', 'price']
    def __init__(self, idnumber, rating, price):
        self.idnumber = idnumber
        self.rating = rating
        self.price = price


slot_start_time = time.time()
slot_books_lst = []
for i in range(n):
    slot_book = MyBookSlots(BookVal(100002), BookVal(9), BookVal(3000))
    slot_books_lst.append(slot_book)
slot_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса со слотами составляет {slot_finish_time - slot_start_time}.")

slot_start_time_change = time.time()
for i in range(n):
    slot_books_lst[i].idnumber.val = BookVal(0)
    slot_books_lst[i].rating.val = BookVal(0)
    slot_books_lst[i].price.val = BookVal(0)
slot_finish_time_change = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов со слотами составляет {slot_finish_time_change - slot_start_time_change}.")

@profile
def slot_memory():
    slot_books_lst = []
    for i in range(n):
        slot_book = MyBookSlots(BookVal(100002), BookVal(9), BookVal(3000))
        slot_books_lst.append(slot_book)
    for i in range(n):
        slot_books_lst[i].idnumber.val  = BookVal(0)
        slot_books_lst[i].rating.val = BookVal(0)
        slot_books_lst[i].price.val = BookVal(0)
slot_memory()

class MyBookWeakref:
    def __init__(self, idnumber, rating, price):
        self._idnumber_ref = weakref.ref(idnumber)
        self._rating_ref = weakref.ref(rating)
        self._price_ref = weakref.ref(price)

    @property
    def idnumber(self):
        return self._idnumber_ref()
    
    @property
    def rating(self):
        return self._rating_ref()
    
    @property
    def price(self):
        return self._price_ref()


weakref_start_time = time.time()
weakref_books_lst = []
idnumber, rating, price = BookVal(100003), BookVal(10), BookVal(5000)
for i in range(n):
    weakref_book = MyBookWeakref(idnumber, rating, price)
    weakref_books_lst.append(weakref_book)
weakref_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса с weakref атрибутами составляет {weakref_finish_time - weakref_start_time}.")

weakref_start_time_change = time.time()
for i in range(n):
    weakref_books_lst[i].idnumber.val += 1
    weakref_books_lst[i].rating.val += 1
    weakref_books_lst[i].price.val += 1

weakref_finish_time_change = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов с weakref атрибутами составляет {weakref_finish_time_change - weakref_start_time_change}.")

@profile
def weakref_memory():
    weakref_books_lst = []
    idnumber, rating, price = BookVal(100003), BookVal(10), BookVal(5000)
    for i in range(n):
        weakref_book = MyBookWeakref(idnumber, rating, price)
        weakref_books_lst.append(weakref_book)
    for i in range(n):
        weakref_books_lst[i].idnumber.val += 1
        weakref_books_lst[i].rating.val += 1
        weakref_books_lst[i].price.val += 1
        
weakref_memory()