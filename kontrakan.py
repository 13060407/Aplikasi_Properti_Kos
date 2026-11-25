
from properti import Properti


class Kontrakan(Properti):
    def __init__(self, id_properti, nama, alamat, harga,
                 jumlah_kamar, luas_bangunan):

        super().__init__(id_properti, nama, alamat, harga)

        self.jumlah_kamar = jumlah_kamar
        self.luas_bangunan = luas_bangunan

    def tampilkan_info(self):
        print("\n===== DATA KONTRAKAN =====")
        super().tampilkan_info()
        print("Jumlah Kamar :", self.jumlah_kamar)
        print("Luas Bangunan:", self.luas_bangunan, "m2")
