class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk} warna {self.warna} ({self.tahun}) - Bahan bakar: {self.bahan_bakar}"


# Instansiasi object
knd1 = Kendaraan("Toyota", "Hitam", 2022)
knd2 = Kendaraan("Honda", "Putih", 2024)

print(knd1.info_kendaraan())
print(knd2.info_kendaraan())
print(f"Bahan bakar: {Kendaraan.bahan_bakar}")