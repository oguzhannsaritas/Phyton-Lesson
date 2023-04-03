from time import time
print("Adınızı Giriniz: ", end="")
baslangicZamani = time()
ad = input()
zaman = time() - baslangicZamani
print(ad, "bilgilerinizi", zaman, "zamanda girdiniz")