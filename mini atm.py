bakiye = 1000
while True:
    print("******************************")
    print("Oğuzhan Banka Hoşgeldiniz...")
    print("******************************")

    print("Bakiye görüntülemek için lütfen '1' tuşuna basınız.")
    print("Hesabınıza para çekmek için lütfen '2' tuşuna basınız.")
    print("Hesabınızdan para yatırmak için lütfen '3' tuşuna basınız.")
    print("Atm'den çıkmak istiyorsanız lütfen '4'tuşuna basınız.")
    islem = input("Yapmak istediğiniz işlemi seçiniz.")

    if islem == "1":
        print("Bakiyeniz :", bakiye)
    elif islem == "2":
        miktar = int(input("Çekmek istedğiniz miktarı giriniz."))
        if miktar > bakiye:
            print("Bakiyeniz yetersizdir.")

    else:
        bakiye -= miktar
        print("Çekmek işlemi başarılı")
        print("Bakiyeniz : ", bakiye)

    if islem == "3":
        miktar = int(input("yatırmak istediğin miktarı giriniz."))
        bakiye += miktar
        print("Bakiyeniz :", bakiye)

    elif islem == "4":
        print("Atm den çıkılıyor")
        break



