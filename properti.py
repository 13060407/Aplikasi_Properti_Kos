
class Properti:
    def __init__(self, id_properti, nama, alamat, harga):
        self.id_properti = id_properti
        self.nama = nama
        self.alamat = alamat
        self.harga = harga

    def tampilkan_info(self):
        print("ID Properti :", self.id_properti)
        print("Nama        :", self.nama)
        print("Alamat      :", self.alamat)
        print("Harga       : Rp", format(self.harga, ",").replace(",", "."))
