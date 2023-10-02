import unittest
from unittest.mock import MagicMock
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

    def test_pass_smth_instead_of_callback(self):
        with self.assertRaises(TypeError):
            parse_json(json_str=self.json_file,
                       required_fields=["smth"],
                       keywords=["smth"],
                       keyword_callback={})
        with self.assertRaises(TypeError):
            parse_json(json_str=self.json_file,
                       required_fields=["smth"],
                       keywords=["smth"],
                       keyword_callback=[])


if __name__ == "__main__":
    unittest.main()
