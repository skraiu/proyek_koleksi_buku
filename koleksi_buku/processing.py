def hitung_total(*angka):
    return sum(angka)

class Buku:
    def __init__(self, judul, pengarang, tahun, stok, **info_tambahan):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
        self.stok = stok
        self.info_tambahan = info_tambahan

    def info(self):
        return f"{self.judul} - {self.pengarang} ({self.tahun}), stok: {self.stok}"

    def apakah_menipis(self, batas=3):
        return self.stok <= batas

class KoleksiBuku:
    def __init__(self):
        self.daftar = []

    def tambah(self, buku):
        assert isinstance(buku, Buku), "Yang ditambahkan harus objek Buku"
        self.daftar.append(buku)

    def total_stok(self):
        return hitung_total(*[b.stok for b in self.daftar])

    def urutkan_tahun(self, terbaru=True):
        return sorted(self.daftar, key=lambda b: b.tahun, reverse=terbaru)

    def stok_menipis(self, batas=3):
        return list(filter(lambda b: b.apakah_menipis(batas), self.daftar))

    def buat_laporan(self):
        baris = ["LAPORAN KOLEKSI BUKU", "=" * 30]
        for b in self.urutkan_tahun():
            baris.append(b.info())
        baris.append("=" * 30)
        baris.append(f"Total judul : {len(self.daftar)}")
        baris.append(f"Total stok  : {self.total_stok()}")
        baris.append(f"Stok menipis: {len(self.stok_menipis())} judul")
        return "\n".join(baris)