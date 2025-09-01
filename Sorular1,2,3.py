"""
Hedef
• Koşullu durumları (if/elif/else) uygulamak
• Döngüler (for, while) ile veri işlemek
• String metotları ve listeler üzerinde alıştırmalar yapmak
• Temel veri işleme becerilerini geliştirmek
"""

# 1.Soru ---------------------------------
"""
sayi = int(input("Kontrol etmek istediğiniz sayıyı giriniz: "))
if sayi>0:
    print("Sayımız pozitif")
    if sayi % 2 == 0:
        print("ve çift")
    else:
        print("ve tek")
elif sayi<0:
    print("Sayımız negatif")
    if sayi % 2 == 0:
        print("ve çift")
    else:
        print("ve tek")
else:
    print("Sayımız sıfırdır ve çifttir.")
"""
# 2.Soru ---------------------------------
""""
kelime = input("Kelimenizi giriniz:")

harf_sayisi = {}

for harf in kelime:
    if harf in harf_sayisi:
        harf_sayisi[harf] += 1
    else:
        harf_sayisi[harf] = 1

print(harf_sayisi)
"""

#3.Soru
sifre = input("Şifrenizi giriniz: ")

#Kontrol Kısmı
uzunluk_ok = len(sifre) >= 8

buyuk_harf_ok = False
for harf in sifre:
    if harf.isupper():
        buyuk_harf_ok = True

rakam_ok = False
for harf in sifre:
    if harf.isdigit():
        rakam_ok = True


if uzunluk_ok and buyuk_harf_ok and rakam_ok:
    print("Şifre uygun!")
else:
    print("Şifre uygun değil!")
    if not uzunluk_ok:
        print("- En az 8 karakter olmalı")
    if not buyuk_harf_ok:
        print("- En az 1 büyük harf olmalı")
    if not rakam_ok:
        print("- En az 1 rakam olmalı")
