import math

def faktor(n):
    return [i for i in range(1, n+1) if n % i == 0]

def hitung_fpb(a, b):
    print("\n--- Penjelasan FPB ---")
    print(f"Faktor dari {a}: {faktor(a)}")
    print(f"Faktor dari {b}: {faktor(b)}")

    faktor_a = set(faktor(a))
    faktor_b = set(faktor(b))

    fpb = max(faktor_a & faktor_b)
    print(f"Faktor sama: {sorted(faktor_a & faktor_b)}")
    print(f"FPB = {fpb}")
    return fpb

def hitung_kpk(a, b, fpb):
    print("\n--- Penjelasan KPK ---")
    print(f"KPK = (a × b) / FPB")
    print(f"KPK = ({a} × {b}) / {fpb}")
    kpk = abs(a * b) // fpb
    print(f"KPK = {kpk}")
    return kpk


while True:
    print("\n=== PROGRAM FPB & KPK DENGAN PENJELASAN ===")

    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus angka!")
        continue

    # Hitung FPB dengan penjelasan
    fpb = hitung_fpb(a, b)

    # Hitung KPK dengan penjelasan
    kpk = hitung_kpk(a, b, fpb)

    print("\n=== HASIL AKHIR ===")
    print(f"FPB = {fpb}")
    print(f"KPK = {kpk}")

    ulang = input("\nHitung lagi? (y/n): ").lower()
    if ulang != "y":
        print("Terima kasih! Program selesai.")
        break