from hashing import Hashing
from performance_analysis import PerformanceAnalysis

def main():
    size = 10
    Hash = Hashing(size)

    Hash.insert_data("Joko", "Mahasiswa")
    Hash.insert_data("Agus", "Guru")
    Hash.insert_data("Lutpi", "Exp")
    Hash.insert_data("Tony stark", "Bilioner")
    Hash.insert_data("Joko", "Manusia")
    Hash.insert_data("Ucok", "Pengusaha")
    Hash.insert_data("Timoti", "Pemegang saham")
    Hash.insert_data("Jokopi", "Pengusaha")
    Hash.insert_data("Joko", "Sigma")

    print(f"Cari 'Joko' : {Hash.search_data('Joko')}")   
    print(f"Cari 'Ucok' : {Hash.search_data('Ucok')}")   
    print(f"Cari 'Lutpi' : {Hash.search_data('Lutpi')}")  
    print(f"Total data tersimpan: {Hash.count}\n")

    analysis = PerformanceAnalysis()
    analysis.analysis_time()


if __name__ == "__main__":
    main()