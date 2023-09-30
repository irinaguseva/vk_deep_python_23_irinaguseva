import unittest
from unittest.mock import MagicMock
from predict_message_mood_func import predict_message_mood, SomeModel


class TestPredictMessageMood(unittest.TestCase):

    def setUp(self):
        self.model = SomeModel()

    def test_predict_message_mood_bad(self):
        self.model.predict = MagicMock(return_value=0.2)
        result = predict_message_mood(
            "Тестируем получение оценки неуд", self.model)
        self.assertEqual(result, 'неуд')

    def test_predict_message_mood_good(self):
        self.model.predict = MagicMock(return_value=0.9)
        result = predict_message_mood(
            "Тестируем получение оценки отл", self.model)
        self.assertEqual(result, 'отл')

    def test_predict_message_mood_normal(self):
        self.model.predict = MagicMock(return_value=0.5)
        result = predict_message_mood(
            "Тестируем получение оценки норм", self.model)
        self.assertEqual(result, 'норм')

    def test_predict_message_mood_with_another_thresholds(self):
        self.model.predict = MagicMock(return_value=1.1)
        result = predict_message_mood(message="This is a normal message",
                                      model=self.model,
                                      bad_thresholds=5, good_thresholds=10)
        self.assertEqual(result, 'неуд')

        self.model.predict = MagicMock(return_value=5.5)
        result = predict_message_mood(message="This is a normal message",
                                      model=self.model,
                                      bad_thresholds=5, good_thresholds=10)
        self.assertEqual(result, 'норм')

        self.model.predict = MagicMock(return_value=11)
        result = predict_message_mood(message="This is a normal message",
                                      model=self.model,
                                      bad_thresholds=5, good_thresholds=10)
        self.assertEqual(result, 'отл')

    def test_predict_message_mood_corner_thresholds(self):
        self.model.predict = MagicMock(return_value=10)
        result = predict_message_mood(message="This is a normal message",
                                      model=self.model,
                                      bad_thresholds=5, good_thresholds=10)
        self.assertEqual(result, 'норм')
        self.model.predict = MagicMock(return_value=5)
        result = predict_message_mood(message="This is a normal message",
                                      model=self.model,
                                      bad_thresholds=5, good_thresholds=10)
        self.assertEqual(result, 'норм')

    def test_predict_message_mood_giving_message_of_wrong_type(self):
        with self.assertRaises(TypeError):
            predict_message_mood(message=[],
                                 model=self.model,
                                 bad_thresholds=0.3,
                                 good_thresholds=0.8)
        with self.assertRaises(TypeError):
            predict_message_mood(message={},
                                 model=self.model,
                                 bad_thresholds=0.3,
                                 good_thresholds=0.8)

    def test_predict_message_mood_giving_smth_instead_of_model(self):
        with self.assertRaises(TypeError):
            predict_message_mood(message='bool_model',
                                 model=True)

    def test_predict_message_mood_giving_bad_threshold_of_wrong_type(self):
        with self.assertRaises(TypeError):
            predict_message_mood(message='incorrect_bad_thresholds',
                                 model=self.model,
                                 bad_thresholds='bad',
                                 good_thresholds=0.8)

    def test_predict_message_mood_giving_good_threshold_of_wrong_type(self):
        with self.assertRaises(TypeError):
            predict_message_mood(message='incorrect_good_thresholds',
                                 model=self.model,
                                 bad_thresholds=0.4,
                                 good_thresholds='good')

    def test_predict_message_mood_giving_incorrect_thresholds(self):
        with self.assertRaises(AssertionError):
            predict_message_mood(message='incorrect_thresholds',
                                 model=self.model,
                                 bad_thresholds=0.5,
                                 good_thresholds=0.1)
        with self.assertRaises(AssertionError):
            predict_message_mood(message='equal_thresholds',
                                 model=self.model,
                                 bad_thresholds=0.5,
                                 good_thresholds=0.5)


if __name__ == '__main__':
    unittest.main()
