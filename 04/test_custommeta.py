import unittest
from custommeta import CustomMeta, CustomClass


class CustomMetaTests(unittest.TestCase):

    def test_cases_provided_in_task_given(self):
        assert CustomClass.custom_x == 50
        with self.assertRaises(AttributeError):
            CustomClass.x
        inst = CustomClass()
        assert inst.custom_x == 50
        assert inst.custom_val == 99
        assert inst.custom_line() == 100
        assert str(inst) == "Custom_by_metaclass"
        with self.assertRaises(AttributeError):
            inst.x
        with self.assertRaises(AttributeError):
            inst.val
        with self.assertRaises(AttributeError):
            inst.line()
        with self.assertRaises(AttributeError):
            inst.yyy
        inst.dynamic = "added later"
        assert inst.custom_dynamic == "added later"
        with self.assertRaises(AttributeError):
            inst.dynamic

    def test_custommeta_class_created(self):
        class TestClass(metaclass=CustomMeta):
            x = '''Let's test the fact our class
                   belongs to CustomMeta'''
        test_obj = TestClass()
        self.assertIsInstance(test_obj, TestClass)

    def test_adding_custom_prefix(self):
        class TestClass(metaclass=CustomMeta):
            waiting_for_a_prefix = 1
        test_obj = TestClass()
        with self.assertRaises(AttributeError):
            test_obj.waiting_for_a_prefix
        self.assertEqual(test_obj.custom_waiting_for_a_prefix, 1)
        self.assertTrue("custom_waiting_for_a_prefix" in TestClass.__dict__)

    def test_setattr(self):
        class TestClass(metaclass=CustomMeta):
            prefix = 1
            __magic__ = 2
        test_obj = TestClass()
        with self.assertRaises(AttributeError):
            test_obj.prefix
        with self.assertRaises(AttributeError):
            test_obj.custom___magic__
        self.assertEqual(test_obj.custom_prefix, 1)
        self.assertTrue("custom_prefix" in TestClass.__dict__)
        self.assertEqual(test_obj.__magic__, 2)
        self.assertTrue("__magic__" in TestClass.__dict__)

    def test_obj_dict(self):
        class TestClass(metaclass=CustomMeta):
            pass
        test_obj = TestClass()
        test_obj.__attr__ = 1
        test_obj.attr = 2
        self.assertEqual(test_obj.__dict__, {'__attr__': 1, 'custom_attr': 2})

    def test_passing_magic(self):
        class TestClass(metaclass=CustomMeta):
            __magic__ = 1
        test_obj = TestClass()
        with self.assertRaises(AttributeError):
            test_obj.custom___magic__
        self.assertEqual(test_obj.__magic__, 1)
        self.assertTrue("__magic__" in TestClass.__dict__)

    def test_check_with_passed_arg(self):
        class TestClass(metaclass=CustomMeta):
            def __init__(self, value):
                self.attr = value
        test_obj = TestClass(5)
        self.assertEqual(test_obj.custom_attr, 5)

    def test_with_class_inherited(self):
        class TestClass(metaclass=CustomMeta):
            x = 3
        class ClassForInheritance(TestClass):
            pass
        test_obj = ClassForInheritance()
        self.assertEqual(test_obj.custom_x, 3)


if __name__ == "__main__":
    unittest.main()
