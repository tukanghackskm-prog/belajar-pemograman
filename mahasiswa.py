class Mahasiswa:
    # 2b. Class attribute
    universitas = "STITEK Bontang"

    # 3a. Constructor dengan instance attributes (2a)
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # 3b. Method perkenalan_diri
    def perkenalan_diri(self):
        return (
            f"Halo, saya {self.nama} (NIM: {self.nim}), "
            f"jurusan {self.jurusan} di {self.universitas} dengan IPK {self.ipk:.2f}."
        )

    # 3c. Method update_ipk
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK {self.nama} berhasil diupdate menjadi {self.ipk:.2f}."
        return "IPK tidak valid. Masukkan nilai antara 0.0 hingga 4.0."

    # 3d. Method predikat_kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Lulus / IPK di bawah batas minimum"


# 4a. Membuat 3 object mahasiswa dengan data berbeda
mhs_1 = Mahasiswa("Dimas Pratama", "TI001", "Teknik Informatika", 3.75)
mhs_2 = Mahasiswa("Siti Aminah", "SI002", "Sistem Informasi", 3.20)
mhs_3 = Mahasiswa("Ahmad Fauzi", "TI003", "Teknik Informatika")

# 4b. Mendemonstrasikan semua method yang ada
print("--- Data Awal & Predikat ---")
for mhs in (mhs_1, mhs_2, mhs_3):
    print(mhs.perkenalan_diri())
    print("Predikat Kelulusan:", mhs.predikat_kelulusan())
    print("-" * 40)

print("--- Demonstrasi update_ipk & Predikat Setelah Update ---")
print(mhs_2.update_ipk(3.60))
print(mhs_2.perkenalan_diri())
print("Predikat Kelulusan:", mhs_2.predikat_kelulusan())
print("-" * 40)

print(mhs_3.update_ipk(2.65))
print(mhs_3.perkenalan_diri())
print("Predikat Kelulusan:", mhs_3.predikat_kelulusan())