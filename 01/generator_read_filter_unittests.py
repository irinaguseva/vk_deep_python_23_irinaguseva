import unittest
import io
from generator_read_filter import generator


class TestGeneratorReadFilter(unittest.TestCase):

    def setUp(self):
        self.test_file = 'generator_robert_burns.txt'
        self.words_to_find = ["deer", "here", "roe"]
        self.expected_result = [
            "My heart isn't here",
            "My heart's in the Highlands a-chasing the deer",
            "A-chasing the wild deer and following the roe"
            ]

    def test_find_all_words_register_the_same(self):
        result = list(generator(self.test_file, self.words_to_find))
        self.assertEqual(result, self.expected_result)

    def test_find_all_words_register_random(self):
        words_we_want_to_find = ["dEeR",
                                 "HeRe",
                                 "ROE"]
        result = list(generator(self.test_file, words_we_want_to_find))
        self.assertEqual(result, self.expected_result)

    def test_give_list_of_nonexistent_words(self):
        words_not_to_be_found = ["abracadabra",
                                 "hollywood",
                                 "ravenclow"]
        expected_result = []
        result = list(generator(self.test_file, words_not_to_be_found))
        self.assertEqual(result, expected_result)

    def test_give_empty_list(self):
        empty_list = []
        expected_result = []
        result = list(generator(self.test_file, empty_list))
        self.assertEqual(result, expected_result)

    def test_give_smth_instead_of_list(self):
        tuple_to_give = ()
        dict_to_give = {}
        set_to_give = set()
        bool_to_give = True
        with self.assertRaises(TypeError):
            list(generator(self.test_file, tuple_to_give))
        with self.assertRaises(TypeError):
            list(generator(self.test_file, dict_to_give))
        with self.assertRaises(TypeError):
            list(generator(self.test_file, set_to_give))
        with self.assertRaises(TypeError):
            list(generator(self.test_file, bool_to_give))

    def test_give_words_of_wrong_type(self):
        list_with_odd_words = [123, True, {}, 'Harry', 'Potter']
        with self.assertRaises(TypeError):
            list(generator(self.test_file, list_with_odd_words))

    def test_wrong_file(self):
        file_really_a_dict = {}
        file_really_a_bool = False
        file_really_a_list = []
        with self.assertRaises(TypeError):
            list(generator(file_really_a_dict, self.words_to_find))
        with self.assertRaises(TypeError):
            list(generator(file_really_a_bool, self.words_to_find))
        with self.assertRaises(TypeError):
            list(generator(file_really_a_list, self.words_to_find))

    def test_io_file_type(self):
        io_file_to_test = io.StringIO()
        io_file_to_test.write(
            "Arma virumque cano\nTroiae que primus ab oris"
        )
        words_to_find_in_io = ['arma', 'primus']
        expected_result_in_io = ['Arma virumque cano',
                                 'Troiae que primus ab oris']
        result = list(generator(io_file_to_test, words_to_find_in_io))
        self.assertEqual(result, expected_result_in_io)

    def test_empty_io_file(self):
        empty_io = io.StringIO()
        result_with_non_empty_list = list(generator(empty_io, ['Arma']))
        self.assertEqual(result_with_non_empty_list, [])
        result_with_empty_list = list(generator(empty_io, []))
        self.assertEqual(result_with_empty_list, [])


if __name__ == "__main__":
    unittest.main()
