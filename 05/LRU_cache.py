class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        if not isinstance(capacity, int):
            raise TypeError('Capacity must be an integer')
        self.cache = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if key not in self.cache:
            return None
        val = self.cache.pop(key)  
        self.cache[key] = val   
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
                del self.cache[next(iter(self.cache))]         
        self.cache[key] = value

    def __getitem__(self, key: int) -> int:
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.set(key, value)
