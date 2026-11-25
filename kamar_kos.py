
from properti import Properti


class KamarKos(Properti):
    def __init__(self, id_properti, nama, alamat, harga,
                 nomor_kamar, fasilitas):

        super().__init__(id_properti, nama, alamat, harga)

        self.nomor_kamar = nomor_kamar
        self.fasilitas = fasilitas
        self.penyewa = None

    def tampilkan_info(self):
        print("\n===== INFORMASI KAMAR KOS =====")
        super().tampilkan_info()
        print("Nomor Kamar :", self.nomor_kamar)
        print("Fasilitas   :", self.fasilitas)

        if self.penyewa is None:
            print("Status      : Tersedia")
        else:
            print("Status      : Terisi")
            print("Penyewa     :", self.penyewa.nama)

    def ditempati_oleh(self, penyewa):
        if self.penyewa is not None:
            print("Maaf, kamar sudah terisi!")
            return False

        if penyewa.kamar is not None:
            print("Penyewa sudah menempati kamar lain!")
            return False

        self.penyewa = penyewa
        penyewa._set_kamar(self)

        print("Penyewa berhasil menempati kamar!")
        return True

    def keluarkan_penyewa(self):
        if self.penyewa is None:
            print("Kamar masih kosong!")
            return

        nama = self.penyewa.nama
        self.penyewa._set_kamar(None)
        self.penyewa = None

        print(nama, "berhasil keluar dari kamar.")
