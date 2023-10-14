class BookName:

    def __init__(self):
        print("BookName.init")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return obj.__dict__[self.name]
    
    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise TypeError("BookName should be a string.")
        if (not all(ord(c) < 128 for c in val)) or len(val) > 99:
            raise ValueError("Wrong symbols in BookName or it's too long.")
        
        obj.__dict__[self.name] = val


class BookAuthor:

    def __init__(self):
        print("BookAuthor.init")

    def __set_name__(self, owner, author):
        self.author = author

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return obj.__dict__[self.author]
    
    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise TypeError("BookAuthor value should be a string.")
        if (not all(ord(c) < 128 for c in val)) or len(val) > 99:
            raise ValueError("Wrong symbols in BookAuthor or it's too long.")
        obj.__dict__[self.author] = val


class BookPrice:

    def __init__(self):
        print("BookAuthor.init")

    def __set_name__(self, owner, price):
        self.price = price

    def __get__(self, obj, objtype):
        if obj is None:
            return None
        return obj.__dict__[self.price]

    def __set__(self, obj, val):
        if not isinstance(val, float) and not isinstance(val, int):
            raise TypeError("BookPrice must be a float or an integer.")
        if val <= 0 or val >= 1000000:
            raise ValueError("BookPrice must be greater than zero and less than 1,000,000.")
        obj.__dict__[self.price] = val


class BritishBooks:

    '''The class BritishBooks represents a book 
       available for purchase on an online 
       marketplace Amazon. It has three descriptors: 
       BookName, BookAuthor, and BookPrice'''
    
    name = BookName()
    author = BookAuthor()
    price = BookPrice()

    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f'The novel {self.name} by {self.author} costs {self.price} $'