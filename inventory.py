class ManajerInventori:
    def __init__(self, nama_gudang, barang=None):
        self.nama_gudang = nama_gudang
        self.inventori = dict(barang) if barang is not None else {}

    def tambah_barang(self, nama_barang, jumlah=1):
        # Menambah stok barang jika jumlah > 0
        if jumlah > 0:
            self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
            return f"Stok {nama_barang} bertambah +{jumlah}. Total stok: {self.inventori[nama_barang]}"
        return "Jumlah penambahan stok harus positif"

    def hapus_barang(self, nama_barang, jumlah=1):
        # Mengurangi stok barang jika tersedia dan jumlah mencukupi
        if nama_barang not in self.inventori:
            return f"Barang '{nama_barang}' tidak ditemukan"
        if jumlah <= 0:
            return "Jumlah pengurangan stok harus positif"
        if jumlah <= self.inventori[nama_barang]:
            self.inventori[nama_barang] -= jumlah
            sisa = self.inventori[nama_barang]
            if sisa == 0:
                del self.inventori[nama_barang]
            return f"Stok {nama_barang} berkurang -{jumlah}. Sisa stok: {sisa}"
        return f"Stok {nama_barang} tidak mencukupi (tersedia: {self.inventori[nama_barang]})"

    def lihat_inventori(self):
        if not self.inventori:
            return f"Inventori {self.nama_gudang} kosong"
        daftar = ", ".join(f"{barang}: {stok}" for barang, stok in self.inventori.items())
        return f"Inventori {self.nama_gudang} -> {daftar}"


# Demonstrasi penambahan dan pengurangan stok
gudang = ManajerInventori("Gudang Utama")

# 1. Penambahan stok
print(gudang.tambah_barang("Laptop", 10))
print(gudang.tambah_barang("Laptop", 5))   # menambah stok barang yang sudah ada
print(gudang.lihat_inventori())

# 2. Pengurangan stok
print(gudang.hapus_barang("Laptop", 4))    # mengurangi sebagian stok (sisa 11)
print(gudang.hapus_barang("Laptop", 11))   # mengurangi sampai habis (sisa 0)
print(gudang.lihat_inventori())