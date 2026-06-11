import time

class Hashing:
    def __init__(self, size):
        self.size = size 
        self.table = []
        self.count = 0
        self.chaining()
        self.time = None

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

        start_search_data = time.perf_counter()
        for pair in self.table[index]:
            if pair[0] == key:
                end_search_data = time.perf_counter()
                time_result = end_search_data - start_search_data
                return pair[1], time_result
        
        return None
    
    def view_hash_table(self):
        for i, bucket in enumerate(self.table):
            if len(bucket) > 0:
                print(f"Indeks {i} : {bucket}")
    