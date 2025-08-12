# Pilihan lagu sederhana dalam Python
lagu = ["Lagu 1 - Judul A", "Lagu 2 - Judul B", "Lagu 3 - Judul C", "Lagu 4 - Judul D"]

print("Pilih Lagu Favorit Anda:")
for i, judul in enumerate(lagu, 1):
    print(f"{i}. {judul}")

pilihan = int(input("Masukkan nomor lagu pilihan Anda: "))
print(f"Anda memilih: {lagu[pilihan-1]}")