
from properti import Properti


class KamarKos(Properti):
    def __init__(self, id_properti, nama, alamat, harga,
                 nomor_kamar, fasilitas):

        super().__init__(id_properti, nama, alamat, harga)

        self.nomor_kamar = nomor_kamar
        self.fasilitas = fasilitas
        self.penyewa = None

    def tampilkan_info(self):
        print("\n===== DATA KAMAR KOS =====")
        super().tampilkan_info()
        print("Nomor Kamar :", self.nomor_kamar)
        print("Fasilitas   :", self.fasilitas)

        if self.penyewa is None:
            print("Status      : Tersedia")
        else:
            print("Status      : Terisi")
            print("Penyewa     :", self.penyewa.nama)
