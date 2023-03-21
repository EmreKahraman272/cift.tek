def butun_sayilar():
    print("""Devam etmek için "d" yazınız""")
    sayi = 0
    sayilar = []
    while True:
            sayi = input("Sayı giriniz:")
            if sayi == "d":
                break
            sayilar.append(int(sayi))
    return sayilar