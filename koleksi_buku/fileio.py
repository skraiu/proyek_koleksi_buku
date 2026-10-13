from .validasi import validasi_buku, DataTidakValidError

def buat_file(nama_file):
    try:
        with open(nama_file, "x"):
            pass
        return True
    except FileExistsError:
        print(f"File '{nama_file}' sudah ada, tidak dibuat ulang.")
        return False

def tambah_data(nama_file, judul, pengarang, tahun, stok):
    validasi_buku(judul, tahun, stok)
    with open(nama_file, "a") as file:
        file.write(f"{judul};{pengarang};{tahun};{stok}\n")

def baca_data(nama_file):
    hasil = []
    try:
        with open(nama_file, "r") as file:
            for no, baris in enumerate(file, start=1):
                try:
                    judul, pengarang, tahun, stok = baris.strip().split(";")
                    tahun, stok = int(tahun), int(stok)
                    validasi_buku(judul, tahun, stok)
                    hasil.append({"judul": judul, "pengarang": pengarang,
                                  "tahun": tahun, "stok": stok})
                except (ValueError, DataTidakValidError) as e:
                    print(f"Baris {no} dilewati: {e}")
    except FileNotFoundError:
        print(f"Error: file data '{nama_file}' belum ada, buat dulu file-nya.")
    return hasil

def tulis_laporan(nama_file, isi):
    with open(nama_file, "w") as file:
        file.write(isi)