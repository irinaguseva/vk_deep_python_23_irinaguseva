import unittest

from descriptors_books import BritishBooks

class TestBritishBook(unittest.TestCase):

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
            tess = BritishBooks("Tess of the d'Urbervilles", "Thomas Hardy"*10, 10.50)
        with self.assertRaises(ValueError):
            gulliver = BritishBooks("Gulliver's Travels", "Jonathan Swift", 1000001)
        with self.assertRaises(ValueError):
            narnia = BritishBooks("The Lion, the Witch, and the Wardrobe", "C. S. Lewis", -15)

    def test_reassignment(self):
        ivanhoe = BritishBooks("Grate Expectations", "George Eliot", 20)
        self.assertTrue(ivanhoe.name == "Grate Expectations")
        self.assertTrue(ivanhoe.author == "George Eliot")
        self.assertTrue(ivanhoe.price == 20)
        ivanhoe.name = "Ivanhoe"
        self.assertTrue(ivanhoe.name == "Ivanhoe")
        ivanhoe.author = "Walter Scott"
        self.assertTrue(ivanhoe.author == "Walter Scott")
        ivanhoe.price = 15
        self.assertTrue(ivanhoe.price == 15)

    def test_dict_correct(self):
        animal_farm = BritishBooks("Animal Farm", "George Orwell", 16)
        self.assertTrue(animal_farm.__dict__["name"] == "Animal Farm")
        self.assertTrue(animal_farm.__dict__["author"] == "George Orwell")
        self.assertTrue(animal_farm.__dict__["price"] == 16)

    def test_str_correct(self):
        dracula = BritishBooks("Dracula", "Bram Stocker", 77)
        assert(str(dracula) == 'The novel Dracula by Bram Stocker costs 77 $'), str(dracula)
    

if __name__ == '__main__':
    unittest.main()
