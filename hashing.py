class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                current_node.value = value
                return False 
            current_node = current_node.next

        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        return True

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None

class Hashing:
    def __init__(self, size):
        self.size = size
        self.table = []
        self.count = 0
        self.separate_chaining()

    def separate_chaining(self):
        for _ in range(self.size):
            self.table.append(LinkedList())

    def hash_function(self, key):
        return abs(hash(key)) % self.size

    def insert_data(self, key, value):
        index = self.hash_function(key)
        if self.table[index].insert(key, value):
            self.count += 1

    def search_data(self, key):
        index = self.hash_function(key)
        return self.table[index].search(key)

    def view_hash_table(self):
        for i in range(self.size):
            current_node = self.table[i].head
            if current_node:
                data = []
                while current_node:
                    data.append(f"[{current_node.key}: {current_node.value}]")
                    current_node = current_node.next
                print(f"Indeks {i} : {' -> '.join(data)}")