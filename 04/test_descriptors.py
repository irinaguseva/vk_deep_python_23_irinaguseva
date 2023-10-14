import unittest

from descriptors_books import BritishBooks

class TestBookName(unittest.TestCase):

    def test_instance(self):
        new_book = BritishBooks("Book", "Unknown", 404)
        assert isinstance(new_book, BritishBooks)
     
    def test_create_a_correct_book(self):
        emma = BritishBooks("Emma", "Jane Austen", 10.50)
        assert emma.name == 'Emma'
        assert emma.price == 10.50
        assert emma.author == "Jane Austen"

    def test_a_book_with_wrong_types_in_fields(self):
        with self.assertRaises(TypeError):
            wuthering_heights = BritishBooks(5.5, "Emily Brontë", 'fddd')
        with self.assertRaises(TypeError):
            orlando = BritishBooks("Orlando", 888, 10.50)
        with self.assertRaises(TypeError):
            frankenstein = BritishBooks("Frankenstein", "Mary Shelley", "fff")

    def test_a_book_with_wrong_values_in_fields(self):
        with self.assertRaises(ValueError):
            robinson_crusoe = BritishBooks("Robinson Crusoe®", "Daniel Defoe", 10.50)
        with self.assertRaises(ValueError):
            alice = BritishBooks("Alice"*100, "Lewis Carroll", 10.50)

        with self.assertRaises(ValueError):
            hobbit = BritishBooks("Hobbit¶", "J. R. R. Tolkien", 10.50)
        with self.assertRaises(ValueError):
            tess = BritishBooks("Tess of the d'Urbervilles"*10, "Thomas Hardy", 10.50)

if __name__ == '__main__':
    unittest.main()