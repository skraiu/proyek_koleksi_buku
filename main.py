from koleksi_buku import fileio, processing

NAMA_DATA = "buku.txt"
NAMA_LAPORAN = "laporan_buku.txt"

if fileio.buat_file(NAMA_DATA):
    fileio.tambah_data(NAMA_DATA, "Dasar Pemrograman", "Budi", 2020, 5)
    fileio.tambah_data(NAMA_DATA, judul="Basis Data", pengarang="Sari", tahun=2022, stok=2)
    fileio.tambah_data(NAMA_DATA, "Statistika", "Dewi", 2018, 8)
    with open(NAMA_DATA, "a") as file:
        file.write("Buku Rusak;Anon;abcd;2\n")

koleksi = processing.KoleksiBuku()
for d in fileio.baca_data(NAMA_DATA):
    koleksi.tambah(processing.Buku(**d))

laporan = koleksi.buat_laporan()
fileio.tulis_laporan(NAMA_LAPORAN, laporan)
print(laporan)