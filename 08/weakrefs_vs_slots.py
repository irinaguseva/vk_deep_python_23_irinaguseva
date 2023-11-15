
import time
import weakref
import cProfile
import pstats
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
    simple_books_lst[i].idnumber.value = BookVal(0)
    simple_books_lst[i].rating.value = BookVal(0)
    simple_books_lst[i].price.value = BookVal(0)
simple_finish_time = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов с обычными атрибутами составляет {simple_finish_time - simple_start_time}.")

@profile
def memory_profiling_simple_class():
    simple_books_lst = []
    for i in range(n):
        simple_book = MyBookSimple(BookVal(100001), BookVal(8), BookVal(1500))
        simple_books_lst.append(simple_book)
    for i in range(n):
        simple_books_lst[i].idnumber.value = BookVal(1)
        simple_books_lst[i].rating.value = BookVal(1)
        simple_books_lst[i].price.value = BookVal(1)
memory_profiling_simple_class()

class MyBookSlots:
    __slots__ = ['idnumber', 'rating', 'price']
    def __init__(self, idnumber, rating, price):
        self.idnumber = idnumber
        self.rating = rating
        self.price = price


slot_start_time = time.time()
slot_books_lst = []
for i in range(n):
    slot_book = MyBookSimple(BookVal(100002), BookVal(9), BookVal(3000))
    slot_books_lst.append(slot_book)
slot_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса со слотами составляет {slot_finish_time - slot_start_time}.")

slot_start_time_change = time.time()
for i in range(n):
    slot_books_lst[i].idnumber.value = BookVal(0)
    slot_books_lst[i].rating.value = BookVal(0)
    slot_books_lst[i].price.value = BookVal(0)
slot_finish_time_change = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов со слотами составляет {slot_finish_time_change - slot_start_time_change}.")

@profile
def memory_profiling_slot_class():
    slot_books_lst = []
    for i in range(n):
        slot_book = MyBookSimple(BookVal(100002), BookVal(9), BookVal(3000))
        slot_books_lst.append(slot_book)
    for i in range(n):
        slot_books_lst[i].idnumber.value = BookVal(0)
        slot_books_lst[i].rating.value = BookVal(0)
        slot_books_lst[i].price.value = BookVal(0)
memory_profiling_slot_class()

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

for i in range(n):
    weakref_book = MyBookSimple(BookVal(100003), BookVal(10), BookVal(5000))
    weakref_books_lst.append(weakref_book)
weakref_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса с weakref атрибутами составляет {weakref_finish_time - weakref_start_time}.")

weakref_start_time_change = time.time()
for i in range(n):
    weakref_books_lst[i].idnumber.value = BookVal(0)
    weakref_books_lst[i].rating.value = BookVal(0)
    weakref_books_lst[i].price.value = BookVal(0)
weakref_finish_time_change = time.time()
print(f"Время изменения атрибутов {n} экземпляров для классов с weakref атрибутами составляет {weakref_finish_time_change - weakref_start_time_change}.")

@profile
def memory_profiling_weakref_class():
    weakref_books_lst = []
    for i in range(n):
        weakref_book = MyBookSimple(BookVal(100003), BookVal(10), BookVal(5000))
        weakref_books_lst.append(weakref_book)
    for i in range(n):
        weakref_books_lst[i].idnumber.value = BookVal(1)
        weakref_books_lst[i].rating.value = BookVal(2)
        weakref_books_lst[i].price.value = BookVal(3)
        
memory_profiling_weakref_class()