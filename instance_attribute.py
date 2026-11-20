class Kendaraan:
    # Class attribute (milik class, dipakai bersama oleh semua object)
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        # Instance attributes (milik tiap object, nilainya bisa berbeda)
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} - {self.warna} ({self.tahun}) | BBM: {self.bahan_bakar}"


knd1 = Kendaraan("Toyota", "Hitam", 2022)
knd2 = Kendaraan("Honda", "Putih", 2024)

# 1. Akses instance attribute: bisa lewat object (knd1.merk), TIDAK bisa lewat class (Kendaraan.merk -> AttributeError)
print("Instance attr knd1:", knd1.merk, knd1.warna, knd1.tahun)
print("Instance attr knd2:", knd2.merk, knd2.warna, knd2.tahun)

# 2. Akses class attribute: bisa lewat class maupun object
print("Class attr via class :", Kendaraan.bahan_bakar)
print("Class attr via knd1  :", knd1.bahan_bakar)
print("Class attr via knd2  :", knd2.bahan_bakar)

# 3. Mengubah class attribute lewat Class -> berdampak ke semua object yang belum meng-override
Kendaraan.bahan_bakar = "Pertamax"
print("\nSetelah Kendaraan.bahan_bakar diubah jadi 'Pertamax':")
print("knd1:", knd1.info_kendaraan())
print("knd2:", knd2.info_kendaraan())

# 4. Mengubah lewat satu object (knd1.bahan_bakar = ...) -> membuat instance attribute baru khusus knd1
knd1.bahan_bakar = "Solar"
print("\nSetelah knd1.bahan_bakar diubah jadi 'Solar':")
print("knd1:", knd1.info_kendaraan())
print("knd2:", knd2.info_kendaraan())
print("Kendaraan.bahan_bakar tetap:", Kendaraan.bahan_bakar)