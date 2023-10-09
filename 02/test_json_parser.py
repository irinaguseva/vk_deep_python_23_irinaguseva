import unittest
from unittest.mock import MagicMock
from collections import defaultdict
from json_parser import parse_json


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        self.json_file = '{"minecraft_friendly_mobs": "Sheep Ocelot Rabbit",' \
                         ' "minecraft_neutral_mobs": "Enderman Llama Wolf",' \
                         ' "minecraft_hostile_mobs": "Zombie Spider Pillager"}'
        self.keyword_callback = MagicMock()

    def test_json_parser_correct_input(self):
        parse_json(json_str=self.json_file,
                   required_fields=["minecraft_friendly_mobs"],
                   keywords=["Ocelot"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_called_with("minecraft_friendly_mobs",
                                                 "Ocelot")
        
    def test_some_fields_keywords(self):
        parse_json(self.json_file, 
                   ["minecraft_friendly_mobs", "minecraft_neutral_mobs"],
                   ["Rabbit", "Ocelot", "Wolf"], 
                   self.keyword_callback)
        calls = [
            unittest.mock.call("minecraft_friendly_mobs", "Rabbit"),
            unittest.mock.call("minecraft_friendly_mobs", "Ocelot"),
            unittest.mock.call("minecraft_neutral_mobs", "Wolf"),
        ]
        self.assertEqual(calls, self.keyword_callback.mock_calls)

    def test_nonexistent_keyword(self):
        parse_json(self.json_file, 
                   ["minecraft_friendly_mobs"],
                   ["Slenderman"], 
                   self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_some_keywords_in_one_line(self):
        parse_json(self.json_file, 
                   ["minecraft_hostile_mobs"],
                   ["Spider", "Pillager", "Zombie"], 
                   self.keyword_callback)
        calls = [
            unittest.mock.call("minecraft_hostile_mobs", "Spider"),
            unittest.mock.call("minecraft_hostile_mobs", "Pillager"),
            unittest.mock.call("minecraft_hostile_mobs", "Zombie"),
        ]
        self.assertEqual(calls, self.keyword_callback.mock_calls)

    def test_case_insensitive_keywords(self):
        parse_json(self.json_file, 
                   ["minecraft_hostile_mobs"],
                   ["zOmbIe", "SPIDER", "piLLAGer"], 
                   self.keyword_callback)
        calls = [
            unittest.mock.call("minecraft_hostile_mobs", "Zombie"),
            unittest.mock.call("minecraft_hostile_mobs", "Spider"),
            unittest.mock.call("minecraft_hostile_mobs", "Pillager"),
        ]
        self.assertEqual(calls, self.keyword_callback.mock_calls)

    def test_json_parser_incorrect_register_of_field(self):
        parse_json(json_str=self.json_file,
                   required_fields=["MineCRAFT_friENDly_mOBs"],
                   keywords=["Ocelot"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_json_parser_nonexistent_field(self):
        parse_json(json_str=self.json_file,
                   required_fields=["chupakabra"],
                   keywords=["Ocelot"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_json_parser_empty_field(self):
        parse_json(json_str=self.json_file,
                   required_fields=[],
                   keywords=["Ocelot"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_only_one_keyword_split(self):
        parse_json(json_str='{"minecraft_main_mob": "Steve"}',
                   required_fields=["minecraft_main_mob"],
                   keywords=["Steve"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_called_with("minecraft_main_mob",
                                                 "Steve")

    def test_keywords_with_long_spaces(self):
        parse_json(json_str='{"minecraft_main_mobs": "Steve       Alex"}',
                   required_fields=["minecraft_main_mobs"],
                   keywords=["Alex"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_called_with("minecraft_main_mobs",
                                                 "Alex")

    def test_empty_keyword_list(self):
        parse_json(json_str=self.json_file,
                   required_fields=["minecraft_friendly_mobs"],
                   keywords=[],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_empty_json_line(self):
        parse_json(json_str='{}',
                   required_fields=[],
                   keywords=["empty_json"],
                   keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()

    def test_incorrect_json_line(self):
        with self.assertRaises(ValueError):
            parse_json(json_str='{"minecraft_invalid_json": "invalid!}',
                       required_fields=[],
                       keywords=["error"],
                       keyword_callback=self.keyword_callback)
            
    def test_required_fields_none(self):
        parse_json(json_str=self.json_file,
                       required_fields=None,
                       keywords=["smth"],
                       keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called()   

    def test_keywords_none(self):
        parse_json(json_str=self.json_file,
                       required_fields=["smth"],
                       keywords=None,
                       keyword_callback=self.keyword_callback)
        self.keyword_callback.assert_not_called() 

    def test_callback_none(self):
        parse_json(json_str=self.json_file,
                       required_fields=["smth"],
                       keywords=["smth"],
                       keyword_callback=None)
        self.keyword_callback.assert_not_called() 

if __name__ == "__main__":
    unittest.main()
