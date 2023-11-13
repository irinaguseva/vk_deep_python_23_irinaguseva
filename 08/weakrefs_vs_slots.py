import time
import weakref

n = 500000

class MyBookSimple():
    def __init__(self, author, title, rating):
        self.author = author
        self.title = title
        self.rating = rating

simple_start_time = time.time()
simple_books = [MyBookSimple('Walter Scott', 'Ivanhoe', '8.5') for x in range(n)]
simple_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса с обычными атрибутами составляет {simple_finish_time - simple_start_time}.")


class MyBookSlots():
    __slots__ = ['author', 'title', 'rating']
    def __init__(self, author, title, rating):
        self.author = author
        self.title = title
        self.rating = rating
slot_start_time = time.time()
slot_books = [MyBookSlots('Ann Radcliff', 'Italian', '9.0') for x in range(n)]
slot_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса со слотами составляет {slot_finish_time - slot_start_time}.")


class BookStr():
    def __init__(self, string):
        self.string = string

class MyBookWeakref():
    def __init__(self, author, title, rating):
        self._author_ref = weakref.ref(author)
        self._title_ref = weakref.ref(title)
        self._rating_ref = weakref.ref(rating)
    @property
    def author(self):
        return self._author_ref()
    @property
    def title(self):
        return self._title_ref()
    @property
    def rating(self):
        return self._rating_ref()

weakref_start_time = time.time()
# weakref_books = [MyBookWeakref('Walter Scott', 'Ivanhoe', '8.5') for x in range(n)]
weakref_books = [MyBookWeakref(BookStr('Walter Scott'), BookStr('Ivanhoe'), BookStr('8.5')) for x in range(n)]
weakref_finish_time = time.time()
print(f"Время выполнения создания {n} экземпляров для класса с weakref атрибутами составляет {weakref_finish_time - weakref_start_time}.")