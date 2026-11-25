
class Penyewa:
    def __init__(self, id_penyewa, nama, no_hp):
        self.id_penyewa = id_penyewa
        self.nama = nama
        self.no_hp = no_hp
        self.kamar = None

    def _set_kamar(self, kamar):
        self.kamar = kamar

    def menempati_kamar(self, kamar):
        return kamar.ditempati_oleh(self)

    def tampilkan_info(self):
        print("\n===== DATA PENYEWA =====")
        print("ID Penyewa  :", self.id_penyewa)
        print("Nama        :", self.nama)
        print("No HP       :", self.no_hp)

        if self.kamar is not None:
            print("Nomor Kamar :", self.kamar.nomor_kamar)
        else:
            print("Kamar       : Belum menempati kamar")
