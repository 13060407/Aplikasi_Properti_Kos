
class Penyewa:
    def __init__(self, id_penyewa, nama, no_hp):
        self.id_penyewa = id_penyewa
        self.nama = nama
        self.no_hp = no_hp
        self.kamar = None

    def menempati_kamar(self, kamar):
        if self.kamar is not None:
            print("Penyewa sudah memiliki kamar!")
            return

        if kamar.penyewa is not None:
            print("Kamar sudah ditempati penyewa lain!")
            return

        self.kamar = kamar
        kamar.penyewa = self

        print(self.nama, "berhasil menempati kamar",
              kamar.nomor_kamar)

    def tampilkan_info(self):
        print("\n===== DATA PENYEWA =====")
        print("ID Penyewa :", self.id_penyewa)
        print("Nama       :", self.nama)
        print("No HP      :", self.no_hp)

        if self.kamar is not None:
            print("Kamar      :", self.kamar.nomor_kamar)
        else:
            print("Kamar      : Belum menempati kamar")

