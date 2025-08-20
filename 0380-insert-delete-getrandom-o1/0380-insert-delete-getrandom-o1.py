class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.stack = []
        
    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        
        self.cache[val] = len(self.stack)
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        last_val, idx = self.stack[-1], self.cache[val]
        # self.cache[val], self.cache[last_val] = self.cache[last_val], idx
        # self.stack[idx], self.stack[-1] = self.stack[-1], self.stack[idx]
        self.stack[idx], self.cache[last_val] = last_val, idx
        self.stack.pop()
        del self.cache[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()