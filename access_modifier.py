class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        self.nim = nim                  # public
        self.nama = nama                # public
        self._semester = semester       # protected
        self.__ipk = ipk                # private

    def get_semester(self):
        return self._semester

    def set_semester(self, semester_baru):
        if semester_baru < 1:
            raise ValueError("Semester harus minimal 1.")
        self._semester = semester_baru

    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus berada di antara 0.0 dan 4.0.")
        self.__ipk = ipk_baru

    def tampilkan_data(self):
        print(f"NIM      : {self.nim}")
        print(f"Nama     : {self.nama}")
        print(f"Semester : {self._semester}")
        print(f"IPK      : {self.__ipk:.2f}")


if __name__ == "__main__":
    mhs1 = Mahasiswa("2401001", "Dimas", 3, 3.75)
    mhs2 = Mahasiswa("2401002", "Misel", 3, 3.85)

    # Mengganti semester dan IPK (bebas dengan angka valid)
    mhs1.set_semester(5)
    mhs1.set_ipk(3.90)

    mhs2.set_semester(6)
    mhs2.set_ipk(3.92)

    print("=== Mahasiswa 1 (Setelah Diubah) ===")
    mhs1.tampilkan_data()

    print("\n=== Mahasiswa 2 (Setelah Diubah) ===")
    mhs2.tampilkan_data()
