from hashing import Hashing
import time
import random
import string

class PerformanceAnalysis:
    def __init__(self, length=7):
        self.length = length
    
    def generate_random_key(self):
        random_key = string.ascii_letters
        return ''.join(random.choice(random_key) for _ in range(self.length))
    
    def analysis_time(self):
        skala_data = [100, 1000, 5000, 10000, 50000]
        print(f"{'Jumlah Data ':<15} | {'Ukuran Tabel':<12} | {'Waktu Insert (detik)':<22} | {'Waktu Search (detik)':<22}")
        print("-" * 78)

        for n in skala_data:
            table_size = int(n/0.7)
            benchmark_hash = Hashing(table_size)

            dataset = [(self.generate_random_key(), f"value{i}") for i in range (n)]
            start_insert_time = time.perf_counter()
            for key, value in dataset:
                benchmark_hash.insert_data(key, value)
            end_insert_time = time.perf_counter()
            insert_time = start_insert_time - end_insert_time

            random_sample = random.sample(dataset, min(100, n))
            start_search_time = time.perf_counter()
            for key, _ in random_sample:
                benchmark_hash.search_data(key)
            end_search_time = time.perf_counter()
            seacrh_time = start_search_time - end_search_time

            print(f"{n:<15} | {table_size:<12} | {insert_time:<22.6f} | {seacrh_time:<22.6f}")