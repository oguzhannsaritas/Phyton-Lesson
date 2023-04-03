print("Yardım Edin ! Bilgisayarım Çalışmıyor.")
cozum = False
while not cozum:
    print("Bilgisayardan Herhangi bir ses geliyormu")
    secim = input("Veya herhangi bir ışık yanıyormu (Y/N)")
    if secim == "N":
        secim = input("Fişe Takılımı ?")
        if secim == "N":
            print("Fişe Takın")
        else:
            secim = input("Açma düğmesine bastınızmı ? (Y/N)")
            if secim == "N":
                print("Açma düğmesine basınız")
            else:
                secim = input("Sigorta atmışmı mı ? (Y/N")
                if secim == "N":
                    print("Sigortaları kontrol edin")
                else:
                    secim = input("Şalterler inmişmi ? (Y/N)")
                    if secim == "N":
                        print("Şalterleri kontrol edin")
                    else:
                        print("Teknik servise başvurun")
                        cozum = True










