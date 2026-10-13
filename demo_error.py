from koleksi_buku import fileio
from koleksi_buku.validasi import validasi_buku, DataTidakValidError

fileio.baca_data("tidak_ada.txt")

try:
    validasi_buku("", 2020, 5)
except DataTidakValidError as e:
    print("Error ditangani:", e)

try:
    fileio.tambah_data("buku.txt", "Buku Uji", "Anon", 2020, -5)
except DataTidakValidError as e:
    print("Error ditangani:", e)

try:
    int("abcd")
except ValueError as e:
    print("Error ditangani:", e)