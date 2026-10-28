# Kalkulator Sederhana dengan Python

print("=== Kalkulator Sederhana ===")

angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    print("Hasil:", angka1 + angka2)
elif operasi == "-":
    print("Hasil:", angka1 - angka2)
elif operasi == "*":
    print("Hasil:", angka1 * angka2)
elif operasi == "/":
    if angka2 != 0:
        print("Hasil:", angka1 / angka2)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Operasi tidak valid!")

