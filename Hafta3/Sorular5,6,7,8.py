#5.Soru---------------------------------------------------
"""
def kelime_sayaci(metin):
    # kelimelere ayırma
    kelimeler = metin.split()

    # Toplam kelime sayısı
    toplam_kelime = len(kelimeler)

    # En uzun kelime
    en_uzun = ""
    for kelime in kelimeler:
        if len(kelime) > len(en_uzun):
            en_uzun = kelime

    kelime_sayilari = {} #en sık geçen
    for kelime in kelimeler:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime] = 1

    en_cok_gecen = ""
    en_yuksek_sayi = 0
    for kelime, sayi in kelime_sayilari.items():
        if sayi > en_yuksek_sayi:
            en_yuksek_sayi = sayi
            en_cok_gecen = kelime

    return toplam_kelime, en_uzun, en_cok_gecen

metin = input("Bir metin girin: ")
toplam, uzun, en_cok_gecen = kelime_sayaci(metin)

print(f"Toplam kelime sayısı: {toplam}")
print(f"En uzun kelime: {uzun}")
print(f"En sık geçen kelime: {en_cok_gecen}")
"""

#6.Soru---------------------------------------------------
"""
sayilar = [5, 12, 7, 18, 24, 3, 16]

def cift_mi(sayi):
    return sayi % 2 == 0

cift_sayilar = list(filter(cift_mi, sayilar))

def kare_al(sayi):
    return sayi ** 2

kareler = list(map(kare_al, cift_sayilar))
sirali_kareler = sorted(kareler, reverse=True)

print("Çift sayılar:", cift_sayilar)
print("Çift sayıların kareleri:", kareler)
print("Azalan sırada kareler:", sirali_kareler)

#daha kısa şekilde yapmak istersem :)
sonuc = sorted(map(lambda x: x**2, filter(lambda x: x%2==0, sayilar)), reverse=True)
print("Sonuç:", sonuc)
"""