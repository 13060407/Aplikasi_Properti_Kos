
from properti import Properti
from kamar_kos import KamarKos
from kontrakan import Kontrakan
from penyewa import Penyewa


print("=" * 45)
print("       APLIKASI PROPERTI DAN KOS")
print("=" * 45)


# Membuat objek KamarKos
kamar1 = KamarKos(
    "K001",
    "Kos Melati",
    "Jl. Mawar No. 10",
    750000,
    "101",
    "AC, WiFi, Kasur"
)

kamar2 = KamarKos(
    "K002",
    "Kos Anggrek",
    "Jl. Melati No. 20",
    650000,
    "102",
    "Kasur, Lemari, WiFi"
)


# Membuat objek Kontrakan
kontrakan1 = Kontrakan(
    "C001",
    "Kontrakan Pak Budi",
    "Jl. Kenanga No. 15",
    1500000,
    3,
    90
)


# Membuat objek Penyewa
penyewa1 = Penyewa(
    "P001",
    "Andi",
    "081234567890"
)

penyewa2 = Penyewa(
    "P002",
    "Siti",
    "082345678901"
)


# Menampilkan data kamar kos
print("\n--- DATA KAMAR KOS ---")
kamar1.tampilkan_info()
kamar2.tampilkan_info()


# Menampilkan data kontrakan
print("\n--- DATA KONTRAKAN ---")
kontrakan1.tampilkan_info()


# Relasi Penyewa menempati KamarKos
print("\n--- PROSES PENYEWAAN ---")
penyewa1.menempati_kamar(kamar1)
penyewa2.menempati_kamar(kamar2)


# Menampilkan data penyewa
print("\n--- DATA PENYEWA ---")
penyewa1.tampilkan_info()
penyewa2.tampilkan_info()


# Menampilkan status kamar setelah ditempati
print("\n--- STATUS KAMAR ---")
kamar1.tampilkan_info()
kamar2.tampilkan_info()


print("\n" + "=" * 45)
print("       PROGRAM SELESAI")
print("=" * 45)
