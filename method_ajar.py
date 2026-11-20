class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn}"

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} mengajar mata kuliah {mata_kuliah}"


# Instansiasi 2 object Dosen
dosen_1 = Dosen("Budi Santoso", "0011223301")
dosen_2 = Dosen("Siti Aminah", "0044556602")

# Pemanggilan method pada masing-masing object
print(dosen_1.perkenalan())
print(dosen_1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))

print(dosen_2.perkenalan())
print(dosen_2.ajar_mata_kuliah("Basis Data"))