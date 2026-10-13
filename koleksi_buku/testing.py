import unittest
from .processing import Buku, KoleksiBuku, hitung_total
from .validasi import validasi_buku, DataTidakValidError

class TestKoleksi(unittest.TestCase):
    def setUp(self):
        self.koleksi = KoleksiBuku()
        self.koleksi.tambah(Buku("A", "Penulis 1", 2018, 5))
        self.koleksi.tambah(Buku("B", "Penulis 2", 2022, 2))

    def test_hitung_total_args(self):
        self.assertEqual(hitung_total(1, 2, 3), 6)

    def test_total_stok(self):
        self.assertEqual(self.koleksi.total_stok(), 7)

    def test_urutkan_tahun(self):
        self.assertEqual(self.koleksi.urutkan_tahun()[0].judul, "B")

    def test_stok_menipis(self):
        self.assertEqual(len(self.koleksi.stok_menipis(batas=3)), 1)

    def test_validasi_stok_negatif(self):
        with self.assertRaises(DataTidakValidError):
            validasi_buku("C", 2020, -1)

    def test_tambah_bukan_buku(self):
        with self.assertRaises(AssertionError):
            self.koleksi.tambah("bukan buku")

if __name__ == "__main__":
    unittest.main()