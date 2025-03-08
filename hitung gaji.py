# Input data pegawai
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
golongan = input("Masukkan Golongan (A/B/C): ").strip().upper()

# Inisialisasi gaji dan bonus
gaji = 0
bonus = 0

# Menentukan gaji dan bonus berdasarkan status dan golongan
if status == "pegawai tetap":
    gaji = 1_000_000
    if golongan == "A":
        bonus = 200_000
    elif golongan == "B":
        bonus = 400_000
    elif golongan == "C":
        bonus = 550_000
elif status == "honor":
    gaji = 750_000
    if golongan == "A":
        bonus = 150_000
    elif golongan == "B":
        bonus = 275_000
    elif golongan == "C":
        bonus = 480_000
else:
    print("Status atau Golongan tidak valid.")
    exit()

# Menghitung total gaji
gaji_total = gaji + bonus

# Menampilkan hasil
print("\n--- Rincian Gaji ---")
print(f"Nama      : {nama}")
print(f"NIK       : {nik}")
print(f"Status    : {status.title()}")
print(f"Golongan  : {golongan}")
print(f"Gaji      : Rp {gaji:,}")
print(f"Bonus     : Rp {bonus:,}")
print(f"Gaji Total: Rp {gaji_total:,}")
