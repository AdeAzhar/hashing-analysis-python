from hashing import Hashing

def main():
    size = 71
    Hash = Hashing(size)

    data_insert_test = [
        ("Andi", "Staff"), ("Andi", "Manager"), ("Citra", "CEO"), ("Dewi", "CTO"), ("Eko", "COO"),
        ("Fani", "Staff"), ("Gita", "Developer"), ("Hadi", "Designer"), ("Indah", "Analyst"), ("Joko", "QA"),
        ("Kiki", "Manager"), ("Lina", "Staff"), ("Miko", "DevOps"), ("Nina", "HR"), ("Oscar", "Finance"),
        ("Putri", "Staff"), ("Qori", "Marketing"), ("Rian", "Support"), ("Sari", "Developer"), ("Tono", "Manager"),
        ("Ulya", "Staff"), ("Vina", "Researcher"), ("Wawan", "Designer"), ("Xena", "Intern"), ("Yuni", "Staff"),
        ("Zaki", "Manager"), ("Ahmad", "QA"), ("Bella", "Developer"), ("Caca", "Staff"), ("Dedi", "CEO"),
        ("Elsa", "Analyst"), ("Fajar", "Staff"), ("Gani", "Marketing"), ("Hana", "Designer"), ("Iwan", "Developer"),
        ("Jihan", "Staff"), ("Kevin", "Manager"), ("Lulu", "HR"), ("Maya", "Finance"), ("Naufa", "Staff"),
        ("Oki", "DevOps"), ("Pia", "Researcher"), ("Rendi", "QA"), ("Siska", "Developer"), ("Tara", "Staff"),
        ("Umar", "Manager"), ("Vera", "Marketing"), ("Windi", "Designer"), ("Xavi", "Intern"), ("Yudi", "Staff")
    ]

    print("--- Insert Data Test ---")
    for key, val in data_insert_test:
        Hash.insert_data(key, val)
        print(f"Inserted: {key}\t -> {val}")

    print("\n--- Search Data Test ---")
    keys_to_search = ["Jihan", "Putri", "Andi"] 
    
    for key in keys_to_search:
        value = Hash.search_data(key)
        print(f"Key '{key}': Value '{value}'")
    print("")

    Hash.view_hash_table()

if __name__ == "__main__":
    main()