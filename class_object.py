class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn}"


# Pembuatan object
dsn1 = Dosen("Dr. Andi Wijaya", "0102038801")
dsn2 = Dosen("Prof. Rina Kusuma", "0405067902")

print(dsn1.perkenalan())
print(dsn2.perkenalan())