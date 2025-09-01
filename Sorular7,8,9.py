#7.Soru----------------------------
"""
kelime = input("Bir kelime giriniz: ")

# Kelimenin tersini alma!!!!!!!!!
ters_kelime = kelime[::-1]

if kelime == ters_kelime:
    print("Palindrom")
else:
    print("Palindrom değil")
"""

#8.Soru----------------------------
"""
kare_sayisi = [sayi**2 for sayi in range(1, 101) if sayi % 3 == 0 and sayi % 5 == 0]

print("Hem 3'e hem 5'e bölünebilen sayıların kareleri:")
print(kare_sayisi)
"""

#9.Soru----------------------------
cumle = input("Bir cümle girin: ")

# Kelimeleri ayırma kısmı
kelimeler = cumle.split()

# Her kelimenin ilk harfini büyük yapma kısmı
yeni_kelimeler = []
for kelime in kelimeler:
    buyuk_kelime = kelime.capitalize()
    yeni_kelimeler.append(buyuk_kelime)

# Yeni cümleyi oluşturma kısmı
yeni_cumle = " ".join(yeni_kelimeler)

print("Orijinal:", cumle)
print("Yeni:", yeni_cumle)