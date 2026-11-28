# relasi aggregation

class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self) -> float | None:
        if not self.daftar_nilai:
            return None
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


def tampilkan_daftar_matakuliah(universitas: Universitas):
    print(f"=== Daftar Mata Kuliah di {universitas.nama} ===")
    for prodi in universitas.programs:
        print(f"\nProgram Studi: {prodi.nama}")
        if prodi.daftar_matakuliah:
            for i, mk in enumerate(prodi.daftar_matakuliah, start=1):
                print(f"  {i}. [{mk.kode}] {mk.nama}")
        else:
            print("  (Belum ada mata kuliah)")
    print("=" * 42)


def tampilkan_daftar_nilai_mahasiswa(semua_mahasiswa: list[Mahasiswa]):
    print("=== Daftar Nilai Setiap Mahasiswa ===")
    for m in semua_mahasiswa:
        print(f"\nMahasiswa: {m.nim} - {m.nama}")
        if m.daftar_nilai:
            for i, n in enumerate(m.daftar_nilai, start=1):
                print(f"  {i}. {n.kode_mk}: {n.skor}")
            rata = m.rata_rata()
            print(f"  Rata-rata keseluruhan: {round(rata, 2) if rata is not None else '-'}")
        else:
            print("  (Belum ada nilai)")
    print("=" * 38)


def tampilkan_rata_rata_mahasiswa(semua_mahasiswa: list[Mahasiswa]):
    print("=== Rata-Rata Nilai Setiap Mahasiswa ===")
    for m in semua_mahasiswa:
        rata = m.rata_rata()
        if rata is not None:
            print(f"  {m.nim} - {m.nama}: {round(rata, 2)}")
        else:
            print(f"  {m.nim} - {m.nama}: Belum ada nilai")
    print("=" * 38)


if __name__ == "__main__":
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_tk = uni.buat_program("Teknik Komputer")

    # Mata kuliah untuk Teknik Informatika
    mk_ti1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk_ti2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk_ti1)
    prodi_ti.tambah_matakuliah(mk_ti2)

    # Mata kuliah untuk Sistem Informasi
    mk_si1 = MataKuliah("SI101", "Sistem Basis Data")
    mk_si2 = MataKuliah("SI102", "Analisis dan Perancangan Sistem")
    prodi_si.tambah_matakuliah(mk_si1)
    prodi_si.tambah_matakuliah(mk_si2)

    # Mata kuliah untuk Teknik Komputer
    mk_tk1 = MataKuliah("TK101", "Arsitektur Komputer")
    mk_tk2 = MataKuliah("TK102", "Jaringan Komputer")
    prodi_tk.tambah_matakuliah(mk_tk1)
    prodi_tk.tambah_matakuliah(mk_tk2)

    # Membuat 3 Mahasiswa dan menambahkan objek Nilai
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("SI101", 90))
    m2.tambah_nilai(Nilai("SI102", 88))

    m3.tambah_nilai(Nilai("TK101", 82))
    m3.tambah_nilai(Nilai("TK102", 86))
    m3.tambah_nilai(Nilai("TI101", 80))

    semua_mahasiswa = [m1, m2, m3]

    # Tampilkan daftar mata kuliah dari setiap Program Studi
    tampilkan_daftar_matakuliah(uni)

    # Tampilkan daftar nilai untuk setiap mahasiswa
    tampilkan_daftar_nilai_mahasiswa(semua_mahasiswa)

    # Tampilkan rata-rata nilai setiap mahasiswa menggunakan method rata_rata()
    tampilkan_rata_rata_mahasiswa(semua_mahasiswa)

    def report_program(prodi: ProgramStudi, daftar_mhs: list[Mahasiswa]):
        print(f"\nProgram Studi: {prodi.nama}")
        print("Matakuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
        print("Mahasiswa dan rata-rata nilai:")
        for m in daftar_mhs:
            relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
        print("-" * 40)

    for p in uni.programs:
        report_program(p, semua_mahasiswa)
