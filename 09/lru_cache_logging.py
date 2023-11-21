import logging
import argparse

logging.basicConfig(filename='cache.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stdout', action='store_true', help='Log to stdout')
parser.add_argument('-f', '--filter', action='store_true', help='Apply custom filter')
args = parser.parse_args()

def custom_filter(record):
    if len(record.getMessage().split()) % 2 == 0:
        return False
    return True

if args.filter:
    logging.getLogger().addFilter(custom_filter)

class LRUCache:

    def __init__(self, capacity: int):
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be an integer")
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if key not in self.cache:
            # Logging get of missing key
            logging.info(f"Get of missing key {key}")
            return None
        val = self.cache.pop(key)
        self.cache[key] = val
        # Logging get of existing key
        logging.debug(f"Get of existing key {key}")
        return val

    def set(self, key: int, value: int) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                # Logging set of missing key when capacity is reached
                logging.warning(f"Set of missing key {key} when capacity is reached")
                del self.cache[next(iter(self.cache))]
        self.cache[key] = value
        # Logging set of existing key
        logging.debug(f"Set of existing key {key}")

    def __getitem__(self, key: int) -> int:
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

if __name__ == "__main__":

    # Test Data
    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.get("k3") 
    cache.get("k2")
    cache.get("k1")
    cache.set("k3", "val3")
    cache.get("k3")
    cache.get("k2")
    cache.get("k1")
    cache["k3"]

    if args.stdout:
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.DEBUG)
        stdout_formatter = logging.Formatter('%(levelname)s - %(message)s')
        stdout_handler.setFormatter(stdout_formatter)
        logging.getLogger().addHandler(stdout_handler)