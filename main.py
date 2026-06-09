from hashing import Hashing
from performance_analysis import PerformanceAnalysis

def main():
    size = 10
    Hash = Hashing(size)

    data_insert_test = [
        ("Joko", "Mahasiswa"),
        ("Agus", "Guru"),
        ("Lutpi", "Exp"),
        ("Tony stark", "Bilioner"),
        ("Joko", "Manusia"),    
        ("Ucok", "Pengusaha"),
        ("Timoti", "Pemegang saham"),
        ("Jokopi", "Pengusaha"),
        ("Joko", "Sigma")
    ]

    print("--- Insert Data Test ---")
    for key, val in data_insert_test:
        Hash.insert_data(key, val)
        print(f"Inserted: {key} -> {val}")

    print("\n--- Search Data Test ---")
    keys_to_search = ["Joko", "Ucok", "Tony stark", "Agus", "Budi"] 
    
    for key in keys_to_search:
        result = Hash.search_data(key)
        print(f"Cari '{key}': {result}")
    print("")

    analysis = PerformanceAnalysis()
    analysis.analysis_time()


if __name__ == "__main__":
    main()