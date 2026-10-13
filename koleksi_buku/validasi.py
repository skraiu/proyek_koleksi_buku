class DataTidakValidError(Exception):
    pass

def validasi_buku(judul, tahun, stok):
    if not judul.strip():
        raise DataTidakValidError("Judul tidak boleh kosong")
    if stok < 0:
        raise DataTidakValidError("Stok tidak boleh negatif")
    return True

if __name__ == "__main__":
    assert validasi_buku("Python Dasar", 2020, 5) is True
    try:
        validasi_buku("", 2020, 5)
    except DataTidakValidError as e:
        print("Pengujian lokal berhasil:", e)