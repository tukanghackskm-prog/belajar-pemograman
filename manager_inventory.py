class ManajerInventori:
    def __init__(self, nama_gudang, barang=None):
        self.nama_gudang = nama_gudang
        # Gunakan dictionary {nama_barang: jumlah} untuk menyimpan stok tiap barang
        self.inventori = dict(barang) if barang is not None else {}

    def tambah_barang(self, nama_barang, jumlah=1):
        if jumlah > 0:
            self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
            return f"Berhasil menambah {jumlah} {nama_barang}. Total stok: {self.inventori[nama_barang]}"
        return "Jumlah barang harus positif"

    def hapus_barang(self, nama_barang, jumlah=1):
        if nama_barang not in self.inventori:
            return f"Barang '{nama_barang}' tidak ditemukan di inventori"
        if jumlah <= 0:
            return "Jumlah barang yang dihapus harus positif"
        if jumlah <= self.inventori[nama_barang]:
            self.inventori[nama_barang] -= jumlah
            sisa = self.inventori[nama_barang]
            if sisa == 0:
                del self.inventori[nama_barang]
            return f"Berhasil menghapus {jumlah} {nama_barang}. Sisa stok: {sisa}"
        return f"Stok {nama_barang} tidak mencukupi (tersedia: {self.inventori[nama_barang]})"

    def lihat_inventori(self):
        if not self.inventori:
            return f"Inventori {self.nama_gudang} kosong"
        daftar = ", ".join(f"{barang}: {stok}" for barang, stok in self.inventori.items())
        return f"Inventori {self.nama_gudang} -> {daftar}"


# Testing
gudang = ManajerInventori("Gudang Utama")
print(gudang.tambah_barang("Keyboard", 10))
print(gudang.tambah_barang("Mouse", 5))
print(gudang.hapus_barang("Keyboard", 3))
print(gudang.lihat_inventori())