giris = 0
toplam = 0
print("Lütfen bir sayı giriniz, negatif sayılar döngüyü sonlandırır:")
while True:
    giris = int(input("sayı : "))
    if giris < 0:
        break # Döngüden çıkılıyor
    toplam += giris
print("Toplam =", toplam)