import math
'''
PROJECT BY GREGORIUS VALERY HERMAWAN PRASETYO.
UNTUK TUGAS INDIVIDU TIK.
'''
def main():
    print("-"*25)
    print(" MENGHITUNG BANGUN RUANG")
    print("-"*25)
    print(" 1. Balok \n 2. Kerucut \n 3. Bola \n")
    x = int(input("Mau hitung yang mana?(1, 2 atau 3) "))

    if x == 1:
        hitung_Balok()
    elif x == 2:
        hitung_kerucut()
    elif x == 3:
        hitung_bola()
    else:
        print("Terimakasih telah mencoba program ini :)")

def hitung_Balok():
    print()
    print("+"*25)
    print(" MENGHITUNG BALOK")
    print("+"*25)
    lebar = float(input("Masukan lebar: "))
    tinggi = float(input("Masukan tinggi: "))
    panjang = float(input("Masukan panjang: "))

    volume = panjang*lebar*tinggi
    Lp = (2*((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)))

    v = int(volume)
    lp = int(Lp)
    print("Volume = {} \nLuas permukaan = {}"  .format(v, lp))
    print()
    loop()

def hitung_kerucut():
    print()
    print("+"*25)
    print(" MENGHITUNG KERUCUT")
    print("+"*25)
    r = float(input("Masukan jari-jari: "))
    t = float(input("Masukan tinggi: "))
    s = math.sqrt((r**2)+(t**2))

    pi = 3.14
    volume = 1/3 * pi * r**2 * t
    Lp = pi * r * (r+s)
    v=int(volume)
    lp=int(Lp)
    print("Volume = {} \nLuas permukaan = {}"  .format(v, lp))
    print()
    loop()

def hitung_bola():
    print()
    print("+"*25)
    print(" MENGHITUNG BOLA ")
    print("+"*25)
    r = float(input("Masukan jari-jari: "))
    t = float(input("Masukan tinggi: "))

    pi = 3.14
    volume = 4/3 * pi * r**3
    Lp = 4 * pi * r**2

    v=int(volume)
    lp=int(Lp)
    print("Volume = {} \nLuas permukaan = {}"  .format(v, lp))
    print()
    loop()

def loop():
    y = True
    while y == True:
        x = input("Mau ulangi lagi?(Y/N) ")

        if x == "Y" or x == "y":
            main()
            print("\n")
        else:
            print("\nTerimakasih telah mencoba program ini :)")
            break
main()