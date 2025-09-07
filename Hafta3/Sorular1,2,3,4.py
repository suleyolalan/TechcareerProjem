""" Hedefler:
• İleri seviye veri yapılarıyla (liste, sözlük, küme) rahatça çalışabilmesi,
• Fonksiyonlar, lambda ve gömülü fonksiyonları etkin kullanabilmesi,
• Modüller ve temel istatistiksel hesaplamaları uygulayabilmesi,
• Kodlarını düzenli ve okunabilir şekilde yazabilmesi,
• Basit bir veri analizi sürecini baştan sona gerçekleştirebilmesi beklenmektedir
"""

#1.Soru----------------------------------------------------------
"""
notlar = [85, 92, 76, 92, 100, 76, 85, 92]

benzersiz_notlar = []
for not_degeri in notlar:
    if not_degeri not in benzersiz_notlar:
        benzersiz_notlar.append(not_degeri)

en_yuksek = max(benzersiz_notlar)
en_dusuk = min(benzersiz_notlar)

sirali_notlar = sorted(benzersiz_notlar) #küçükten büyüğe

print("Orijinal notlar:", notlar)
print("Benzersiz notlar:", benzersiz_notlar)
print("En yüksek not:", en_yuksek)
print("En düşük not:", en_dusuk)
print("Sıralı notlar:", sirali_notlar)
"""
#2.Soru--------------------------------------------------------
"""
def armstrong_kontrol(sayi):
    # string'e çevirip basamak sayısını bulma
    sayi_str = str(sayi)
    basamak_sayisi = len(sayi_str)

    # Her basamağın küpünün toplamını hesaplama
    toplam = 0
    for basamak in sayi_str:
        toplam += int(basamak) ** basamak_sayisi

    # Kontrol 
    if toplam == sayi:
        return True
    else:
        return False

sayi = int(input("Kontrol edilecek sayıyı girin: "))

if armstrong_kontrol(sayi):
    print(f"{sayi} Armstrong sayısı!")
else:
    print(f"{sayi} Armstrong sayısı değil!")
"""
"""
# Örnek sayılar
print("\n--- Örnek testler ---")
test_sayilari = [153, 371, 407, 123, 9474]
for test_sayi in test_sayilari:
    if armstrong_kontrol(test_sayi):
        print(f"{test_sayi}: Armstrong sayısı")
    else:
        print(f"{test_sayi}: Armstrong sayısı değil")
"""

#3.Soru---------------------------------------------------------
A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

# kesişim
ortak_diller = A & B

sadece_A = A - B

# birleşim, alfabetik sırada
birlesim = A | B
birlesim_sirali = sorted(birlesim)

print("Ortak diller:", ortak_diller)
print("Sadece A'da olan diller:", sadece_A)
print("Alfabetik birleşim:", birlesim_sirali)

#4.Soru---------------------------------------------------------
import random
import statistics

sayilar = []
for i in range(10):
    rastgele_sayi = random.randint(1, 100)
    sayilar.append(rastgele_sayi)

ortalama = statistics.mean(sayilar)
standart_sapma = statistics.stdev(sayilar)

print("Üretilen 10 rastgele sayı:")
print(sayilar)
print()
print(f"Ortalama: {ortalama:.2f}")
print(f"Standart sapma: {standart_sapma:.2f}")
