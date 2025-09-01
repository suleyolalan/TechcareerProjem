#Bölüm3 Mini Proje
#9.Soru

ekmek = int(input("Ekmeğin fiyatı :"))
peynir = int(input("Peynirin fiyatı :"))
zeytin = int(input("Zeytinin fiyatı :"))
toplam_fiyat = ekmek + peynir + zeytin

if toplam_fiyat > 200:
    yeni_fiyat = toplam_fiyat - (toplam_fiyat * 0.1)
    print("İndirim kazandınız.Ödeyeceğiniz tutar: ",yeni_fiyat)
else:
    print(toplam_fiyat)


#10.Soru
yıl = int(input("Hangi klasmandayız öğrenelim. Doğum yılını yazabilir misin? :"))
yas = int(2025 - yıl)

if 0<=yas<=12:
    print("Siz bir çocuksunuz")
elif 13<=yas<=17:
    print("Siz bir ergensiniz :) ")
else:
    print("Siz bir yetişkinsiniz..")