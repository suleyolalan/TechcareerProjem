yorumlar = []
print("Film yorumlarınızı girin (5-6 yorum):")

for i in range(5):
    yorum = input(f"{i+1}. yorum: ")
    yorumlar.append(yorum)

# Toplam yorum sayısı
toplam_yorum = len(yorumlar)

# "iyi" geçen yorum sayısı
iyi_sayisi = 0
for yorum in yorumlar:
    if "iyi" in yorum.lower():
        iyi_sayisi += 1


en_uzun = yorumlar[0]
en_kisa = yorumlar[0]

for yorum in yorumlar:
    if len(yorum) > len(en_uzun):
        en_uzun = yorum
    if len(yorum) < len(en_kisa):
        en_kisa = yorum

#Ortalama uzunluk
toplam_uzunluk = 0
for yorum in yorumlar:
    toplam_uzunluk += len(yorum)

ortalama_uzunluk = toplam_uzunluk / toplam_yorum


print("\n--- ANALİZ SONUÇLARI ---")
print(f"Toplam yorum sayısı: {toplam_yorum}")
print(f'"iyi" geçen yorum sayısı: {iyi_sayisi}')
print(f"En uzun yorum: {en_uzun}")
print(f"En kısa yorum: {en_kisa}")
print(f"Ortalama uzunluk: {ortalama_uzunluk} karakter")