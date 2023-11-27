def main():
    print("-"*25)
    print(" MENGHITUNG BANGUN RUANG")
    print("-"*25)
    print(" 1. Balok \n 2. Kerucut \n 3. Bola \n")
    x = int(input("Mau hitung yang mana?(1, 2 atau 3) "))

    if x == 1:
        hitung_Balok()
    else:
        pass

def hitung_Balok():
    print()
    print("+"*25)
    print(" MENGHITUNG BALOK")
    print("+"*25)
    lebar = int(input("Masukan lebar: "))
    tinggi = int(input("Masukan tinggi: "))
    panjang = int(input("Masukan panjang: "))

    volume = panjang*lebar*tinggi
    Lp = (2*((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)))

    print("Volume = {} \nLuas permukaan = {}"  .format(volume, Lp))

        

main()

