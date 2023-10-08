import unittest
from random import randint, random
from itertools import zip_longest
from unittest import TestCase
from customlist import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.lst1_integer = CustomList([randint(0, 10) for x in range(10)])
        self.lst2_integer = CustomList([randint(0, 10) for y in range(10)])

    def test_adding_ints(self):
        ans_for_ints = [(a + b) for a, b in zip_longest(
                self.lst1_integer.data,
                self.lst2_integer.data,
            )
        ]
        self.assertEqual((self.lst1_integer + CustomList()).data, self.lst1_integer.data)
        self.assertEqual((CustomList([8]) + CustomList([1, 3])).data, [9, 3])
        self.assertEqual((self.lst1_integer + CustomList()).data, self.lst1_integer.data)
        self.assertEqual((self.lst1_integer + self.lst2_integer).data, ans_for_ints)

    def test_adding_floats(self):
        lst1_float = CustomList([random() for x in range(10)])
        lst2_float = CustomList([random() for x in range(10)])
        ans_for_floats = [(a + b) for a, b in zip_longest(
                lst1_float.data,
                lst2_float.data,
            )
        ]
        self.assertEqual((lst1_float + lst2_float).data, ans_for_floats)
        self.assertEqual((CustomList([8.5]) + CustomList([1.0, 3.0])).data, [9.5, 3.0])
        self.assertEqual((lst1_float + CustomList()).data, lst1_float.data)
        self.assertEqual((lst1_float + lst2_float).data, ans_for_floats)

    def test_right_addition(self):
        self.assertEqual(([] + self.lst1_integer).data, self.lst1_integer.data)
        self.assertEqual(([6, 7] + CustomList([8, 9])).data, [14, 16])
        self.assertEqual(([9] + CustomList([1])).data, [10])

    def test_right_addition_with_floats(self):
        self.assertEqual(([2.2, 3.3, 4.4] + CustomList([1])).data, [3.2, 3.3, 4.4])

    def test_basic_addition(self):
        with self.assertRaises(TypeError):
            _ = self.lst1_integer + 1
        with self.assertRaises(TypeError):
            _ = None + self.lst1_integer
        with self.assertRaises(TypeError):
            _ = self.lst1_integer + "string"

        some_custom_list = CustomList()
        self.assertFalse(some_custom_list is (some_custom_list + self.lst1_integer))
        self.assertFalse(some_custom_list is (self.lst1_integer + some_custom_list))
        self.assertFalse(some_custom_list is ([] + some_custom_list))
        self.assertFalse(some_custom_list is (some_custom_list + []))
        self.assertFalse(some_custom_list is ([1, 2, 4] + some_custom_list))
        self.assertFalse(some_custom_list is (some_custom_list + [3, 4, 5]))
    
    def test_subtract_ints(self):
        ans_for_ints = [
            (a - b)
            for a, b in zip_longest(
                self.lst1_integer.data,
                self.lst2_integer.data,
            )
        ]
        self.assertEqual((self.lst1_integer - self.lst2_integer).data, ans_for_ints)
        
    def test_subtract_floats(self):
        lst1_float = CustomList([random() for x in range(10)])
        lst2_float = CustomList([random() for x in range(10)])
        ans_for_floats = [
            (a - b)
            for a, b in zip_longest(
                lst1_float.data,
                lst2_float.data,
            )
        ]
        self.assertEqual((lst1_float - lst2_float).data, ans_for_floats)

    def test_subtract_lists_of_dif_sizes(self):
        lst = CustomList([1, 2, 3])
        self.assertEqual((lst - CustomList([2])).data, [-1, 2, 3])
        self.assertEqual(
            (lst - CustomList([2, 5, 4, 7])).data, [-1, -3, -1, -7]
        )
        self.assertEqual((lst - [2]).data, [-1, 2, 3])
        self.assertEqual((lst - [2, 5, 4, 7]).data, [-1, -3, -1, -7])

    def test_subtract_empty_lists(self):
        self.assertEqual((self.lst1_integer - []).data, self.lst1_integer.data)
        self.assertEqual((self.lst1_integer - CustomList()).data, self.lst1_integer.data)

    def test_right_subtraction_same_size(self):
        lst = list(range(10))
        expected_result = [
            x_val - y_val
            for x_val, y_val in zip_longest(
                lst,
                self.lst2_integer.data,
            )
        ]
        self.assertEqual((lst - self.lst2_integer).data, expected_result)

    def test_right_subtract_lists_of_dif_size(self):
        lst = list(range(10))
        expected_result = [
            x_val - y_val
            for x_val, y_val in zip_longest(
                lst,
                self.lst2_integer.data,
            )
        ]
        # вычитание из списка другого размера
        some_custom_list = CustomList([1, 2, 3])
        self.assertEqual(([1] - some_custom_list).data, [0, -2, -3])
        self.assertEqual(([3, 2] - some_custom_list).data, [2, 0, -3])
        self.assertEqual(([5, 3, 2, 7] - some_custom_list).data, [4, 1, -1, 7])

    def test_right_subtraction_empty_list(self):
        # вычитание из пустых списков
        expected_result = [item * (-1) for item in self.lst2_integer.data]
        self.assertEqual(([] - self.lst2_integer).data, expected_result)
        self.assertEqual((CustomList() - self.lst2_integer).data, expected_result)

    def test_basic_subtraction(self):
        with self.assertRaises(TypeError):
            _ = self.lst1_integer - 1

        with self.assertRaises(TypeError):
            _ = None - self.lst1_integer
    
    def test_new_object_created(self):
        lst_to_check_new_obj = CustomList()
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj - self.lst1_integer))
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj - []))
        self.assertFalse(lst_to_check_new_obj is
                         ([1, 2, 3] - lst_to_check_new_obj))

    def test_equal(self):
        lst1 = CustomList([1, 2, 3])  # 6
        lst2 = CustomList([4, 5, 6])  # 15
        lst3 = CustomList([7, -1])  # 6
        lst4 = CustomList([4, 2, 0])  # 6
        self.assertEqual(lst1, lst3)
        self.assertEqual(lst1, lst4)
        self.assertNotEqual(lst1, lst2)

    def test_greater(self):
        lst1 = CustomList([6, 7])
        lst2 = CustomList([7, 8])
        self.assertGreater(lst2, lst1)

    def test_greater_equal(self):
        lst1 = CustomList([6, 7])
        lst2 = CustomList([7, 8])
        lst3 = CustomList([16])
        self.assertGreater(lst2, lst1)
        self.assertGreaterEqual(lst2, lst1)
        self.assertGreaterEqual(lst3, lst2)

    def test_less(self):
        lst1 = CustomList([2, 4])
        lst2 = CustomList([3, 5]) 
        self.assertLess(lst1, lst2)

    def test_less_equal(self):
        lst1 = CustomList([2, 4])
        lst2 = CustomList([3, 3])
        lst3 = CustomList([3, 6])
        self.assertLessEqual(lst1, lst2)
        self.assertLessEqual(lst2, lst3)

    def test_wrong_operators(self):
        cust_list_for_wrong_ops = CustomList([404])
        with self.assertRaises(TypeError):
            equal_right = cust_list_for_wrong_ops == 1
        with self.assertRaises(TypeError):
            non_equal_left = cust_list_for_wrong_ops != 2
        with self.assertRaises(TypeError):
            less_eq_right= cust_list_for_wrong_ops <= 3
        with self.assertRaises(TypeError):
            more_eq_left = cust_list_for_wrong_ops >= 4
        with self.assertRaises(TypeError):
            more_right= cust_list_for_wrong_ops > 5
        with self.assertRaises(TypeError):
            less_left = cust_list_for_wrong_ops < 6

    def test_str_non_empty(self):
        self.assertEqual(
            str(CustomList([28, 82])), "CustomList([28, 82], sum = 110)")

    def test_str_empty(self):
        self.assertEqual(str(CustomList([])), "CustomList([], sum = 0)")


if __name__ == "__main__":
    unittest.main()