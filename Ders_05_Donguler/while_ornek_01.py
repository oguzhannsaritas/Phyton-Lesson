sayac = 0
giris= "Y"
while giris!= "N" and giris!= "n":
    print(sayac)
    giris= input("Devam etmek için 'Y' – çıkmak için 'N' giriniz:")
    if giris == "Y" or giris == "y":
        sayac += 1
    elif giris != "N" and giris != "n":
        print("" + giris + "geçerli bir giriş kodu değil")






sayi = 0
toplam = 0
print("Bir sayı giriniz, negatif sayı döngüyü sonlandırır:")
while sayi >= 0:
 sayi= int(input())
 toplam += sayi
 print("Toplam=", toplam)