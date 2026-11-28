class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


if __name__ == "__main__":
    # 2 mata kuliah
    mk1 = MataKuliah("TI101", "Pemrograman Berorientasi Objek")
    mk2 = MataKuliah("TI102", "Basis Data")

    # 3 mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    # Daftarkan mahasiswa ke masing-masing mata kuliah
    mk1.tambah_mahasiswa(m1)
    mk1.tambah_mahasiswa(m2)
    mk1.tambah_mahasiswa(m3)

    mk2.tambah_mahasiswa(m1)
    mk2.tambah_mahasiswa(m3)

    # Tampilkan daftar mahasiswa dan jumlah mahasiswanya
    for mk in (mk1, mk2):
        daftar = mk.daftar_mahasiswa()
        jumlah = mk.jumlah_mahasiswa()
        print(f"Mata Kuliah: {mk.kode} - {mk.nama}")
        print(f"Daftar Mahasiswa ({jumlah} orang): {', '.join(daftar) if daftar else 'Belum ada'}")
        print("-" * 40)
