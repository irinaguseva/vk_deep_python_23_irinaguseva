import unittest

from LRU_cache import LRUCache

class LRUCacheTest(unittest.TestCase):

    def test_the_cases_given(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2") 
        assert cache.get("k3") is None
        assert cache.get("k2") == "val2"
        assert cache.get("k1") == "val1"
        cache.set("k3", "val3")
        assert cache.get("k3") == "val3"
        assert cache.get("k2") is None
        assert cache.get("k1") == "val1"
        assert cache["k3"] == "val3"

    def test_get_key_that_exists(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        result = cache.get("k1")
        self.assertEqual(result, "val1")

    def test_get_nonexistent_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        result = cache.get("k3")
        self.assertIsNone(result)

    def test_update_value_for_key_via_set(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1", "upd_val1")
        result = cache.get("k1")
        self.assertEqual(result, "upd_val1")

    def test_set_new_key_when_cache_full(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        result = cache.get("k3")
        self.assertEqual(result, "val3")

    def test_get_the_key_removed(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        result = cache.get("k1")
        self.assertIsNone(result)

    def test_getitem_existing_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        result = cache["k2"]
        self.assertEqual(result, "val2")

    def test_update_value_for_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache["k1"] = "new_val1"
        result = cache.get("k1")
        self.assertEqual(result, "new_val1")

    def test_set_invalid_capacity_type(self):
        with self.assertRaises(TypeError):
            cache = LRUCache('capacity')  
        with self.assertRaises(TypeError):
            cache = LRUCache([])  

    def test_set_invalid_capacity_value(self):
        with self.assertRaises(ValueError):
            cache = LRUCache(0)  
        with self.assertRaises(ValueError):
            cache = LRUCache(-1)  

    def test_set_invalid_key(self):
        cache = LRUCache(2)
        with self.assertRaises(TypeError):
            cache.set(None, "key_invalid")  

    def test_set_invalid_value(self):
        cache = LRUCache(2)
        with self.assertRaises(TypeError):
            cache.set("k1", None)  

    def test_getitem_invalid_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        with self.assertRaises(TypeError):
            result = cache[None]  


if __name__ == '__main__':
    unittest.main()