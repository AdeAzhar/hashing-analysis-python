class Hashing:
    def __init__(self, size):
        self.size = size
        self.table = []
        self.count = 0
        self.chaining()

    def chaining(self):
        for _ in range(self.size):
            self.table.append([])
    
    def hash_function(self, key):
        return abs(hash(key)) % self.size
    
    def insert_data(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[index].append([key, value])
        self.count +=1

    def search_data(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
            
        return None
    