import unittest

from unittest import TestCase
from customlist import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.lst1_integer = CustomList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.lst2_integer = CustomList([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])

    def test_adding_ints(self):
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer + CustomList(), self.lst1_integer)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(CustomList([8]) + CustomList([1, 3]), [9, 3])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer + CustomList(), self.lst1_integer)))

    def test_adding_floats(self):
        lst1_add_float = CustomList([0.5, 0.6, 0.7])
        lst2_add_float = CustomList([0.5, 0.4, 0.3])
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(CustomList([8.5]) + CustomList([1.0, 3.0]), [9.5, 3.0])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst1_add_float + CustomList(), lst1_add_float)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst1_add_float + lst2_add_float, [1.0, 1.0, 1.0])))

    def test_right_addition(self):
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([] + self.lst1_integer, self.lst1_integer)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([6, 7] + CustomList([8, 9]), [14, 16])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([9] + CustomList([1]), [10])))

    def test_right_addition_with_floats(self):
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([2.2, 3.3, 4.4] + CustomList([1]), [3.2, 3.3, 4.4])))

    def test_add_empty(self):
        empty_list = CustomList()
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(empty_list + self.lst1_integer, self.lst1_integer)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer + empty_list, self.lst1_integer)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(empty_list + [], [])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([] + empty_list, [])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([1, 2, 4] + empty_list, [1, 2, 4])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(empty_list + [3, 4, 5], [3, 4, 5])))
        
    def test_subtract_ints(self):
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer - self.lst2_integer, 
                                [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3])))
        
    def test_subtract_floats(self):
        lst1_float = CustomList([0.5, 0.6, 0.7])
        lst2_float = CustomList([0.5, 0.4, 0.3])
        ans_for_floats = [(a - b) for a, b in zip(lst1_float,lst2_float)]
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst1_float - lst2_float, ans_for_floats)))

    def test_subtract_lists_of_dif_sizes(self):
        lst = CustomList([1, 2, 3])
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst - CustomList([2]), [-1, 2, 3])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst - CustomList([2, 5, 4, 7]), [-1, -3, -1, -7])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst - [2], [-1, 2, 3])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst - [2, 5, 4, 7], [-1, -3, -1, -7])))

    def test_subtract_empty_lists(self):
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer - [], self.lst1_integer)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(self.lst1_integer - CustomList(), self.lst1_integer)))

    def test_right_subtraction_same_size(self):
        lst = list(range(10))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst - self.lst2_integer, 
                                [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2])))

    def test_right_subtract_lists_of_dif_size(self):
        lst_for_testing_dif_sizes = CustomList([1, 2, 3])
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([1] - lst_for_testing_dif_sizes, [0, -2, -3])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([3, 2] - lst_for_testing_dif_sizes, [2, 0, -3])))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([5, 3, 2, 7] - lst_for_testing_dif_sizes, [4, 1, -1, 7])))

    def test_right_subtraction_empty_list(self):
        expected_result = [item * (-1) for item in self.lst2_integer]
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip([] - self.lst2_integer, expected_result)))
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(CustomList() - self.lst2_integer, expected_result)))

    def test_new_object_created_add(self):
        lst_to_check_new_obj = CustomList()
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj + self.lst1_integer))
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj + []))
        self.assertFalse(lst_to_check_new_obj is
                         ([1, 2, 3] + lst_to_check_new_obj))
    
    def test_new_object_created_subtr(self):
        lst_to_check_new_obj = CustomList()
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj - self.lst1_integer))
        self.assertFalse(lst_to_check_new_obj is
                         (lst_to_check_new_obj - []))
        self.assertFalse(lst_to_check_new_obj is
                         ([1, 2, 3] - lst_to_check_new_obj))
        
    def test_old_object_not_changed(self):
        lst_1 = CustomList([1, 2, 3, 4, 5])
        lst_1_save_data = [x for x in lst_1]
        adding = CustomList([1, 2]) + lst_1
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst_1, lst_1_save_data)))
        r_adding = lst_1 + CustomList([])
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst_1, lst_1_save_data)))
        subtr = CustomList([1, 2]) - lst_1
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst_1, lst_1_save_data)))
        r_subtr = lst_1 - CustomList([])
        self.assertTrue(all(elem1 == elem2 for elem1, elem2 in 
                            zip(lst_1, lst_1_save_data)))

    def test_equal(self):
        lst1_for_eq = CustomList([5]) 
        lst2_for_eq = CustomList([2, 3])  
        self.assertEqual(lst1_for_eq, lst2_for_eq)
        lst3_for_eq = CustomList([3, 2]) 
        lst4_for_eq = CustomList([4, 2, 0])  
        self.assertEqual(lst2_for_eq, lst3_for_eq)
        self.assertNotEqual(lst1_for_eq, lst4_for_eq)

    def test_greater(self):
        lst1_for_gr = CustomList([6, 7])
        lst2_for_gr = CustomList([7, 8])
        self.assertGreater(lst2_for_gr, lst1_for_gr)

    def test_greater_equal(self):
        lst1_gr_eq = CustomList([6, 7])
        lst2_gr_eq = CustomList([7, 8])
        self.assertGreater(lst2_gr_eq, lst1_gr_eq)
        lst3_gr_eq = CustomList([16])
        self.assertGreaterEqual(lst2_gr_eq, lst1_gr_eq)
        self.assertGreaterEqual(lst3_gr_eq, lst2_gr_eq)

    def test_less(self):
        lst1_less = CustomList([2, 4])
        lst2_less = CustomList([3, 5]) 
        self.assertLess(lst1_less, lst2_less)

    def test_less_equal(self):
        lst1_l_e = CustomList([2, 4])
        lst2_l_e = CustomList([3, 3])
        self.assertLessEqual(lst1_l_e, lst2_l_e)
        lst3_l_e = CustomList([3, 6])
        self.assertLessEqual(lst2_l_e, lst3_l_e)

    def test_adding_wrong_types_with_ints(self):
        with self.assertRaises(TypeError):
            lst_plus_int = self.lst1_integer + 1
        with self.assertRaises(TypeError):
            lst_plus_lst = {} + self.lst1_integer
        with self.assertRaises(TypeError):
            lst_plus_str = self.lst1_integer + "string"
        with self.assertRaises(TypeError):
            str_plus_lst = "string" + self.lst1_integer 

    def test_adding_wrong_types_with_floats(self):
        with self.assertRaises(TypeError):
            lst_minus_int = self.lst1_integer - 1
        with self.assertRaises(TypeError):
            dic_minus_lst = {} - self.lst1_integer
        with self.assertRaises(TypeError):
            lst_minus_str = self.lst1_integer - "string"
        with self.assertRaises(TypeError):
            str_minus_lst = "string" - self.lst1_integer

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
            str(CustomList([28, 82])), "CustomList: [28, 82], summa: 110")

    def test_str_empty(self):
        self.assertEqual(str(CustomList([])), "CustomList: [], summa: 0")


if __name__ == "__main__":
    unittest.main()