#4.Soru-----------------------------
"""
liste = [12, 4, 9, 25, 30, 7, 18]

# Ortalama hesapladığım kısım
toplam = sum(liste)
ortalama = toplam / len(liste)

# Ortalamadan büyük sayıları bulma
buyuk_sayilar = []
for sayi in liste:
    if sayi > ortalama:
        buyuk_sayilar.append(sayi)

print("Ortalama:", ortalama)
print("Ortalamadan büyük sayılar:", buyuk_sayilar)
"""

#5.Soru-----------------------------
"""
# Üçgen desen
for i in range(1, 6):  # 1'den 5'e kadar!
    for j in range(i):  
        print("*", end="")
    print() 
"""

#6.Soru-----------------------------
"""
toplam = 0
adet = 0

while True:
    sayi = int(input("Bir sayı giriniz: "))

    if sayi == 0:
        break

    toplam += sayi
    adet += 1

if adet > 0:
    ortalama = toplam / adet
    print("Toplam:", toplam)
    print("Ortalama:", ortalama)
else:
    print("Hiç sayı girilmedi.")
"""
