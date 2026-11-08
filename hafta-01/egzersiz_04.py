# ============================================================
# HAFTA 1 — EGZERSİZ 4
# Konu: input() ile kullanıcıdan veri alma
# Süre: ~30 dakika
# ============================================================
#
# input() NEDİR?
# Programı durdurur ve kullanıcıdan bir şey yazmasını bekler.
# Kullanıcı Enter'a basınca devam eder.
#
# Örnek:
#   isim = input("Adın ne? ")
#   print(f"Merhaba, {isim}!")
#
# ÖNEMLİ:
# input() her zaman metin (str) döndürür.
# Sayı istiyorsan int() veya float() ile çevirmen gerekir.
#   yas = int(input("Yaşın kaç? "))
# ============================================================


# --- BÖLÜM 1: İlk input ---

# Bu satırlar zaten çalışıyor. Çalıştır ve dene:
isim = input("Adın ne? ")
print(f"Merhaba, {isim}!")

# TODO 1: Kullanıcıdan şehrini al ve yazdır:
# "İstanbul'dan mısın harika!"  gibi bir cümle kur.
# (Şehir adı değişkenden gelmeli.)
sehir = input("nerelisin? ")
print(f"{sehir}'den misin? güzel.")

# --- BÖLÜM 2: Sayı alma ---

# TODO 2: Kullanıcıdan yaşını al.
# int() ile sayıya çevir.
# Sonra şunu yazdır:
# "10 yıl sonra X yaşında olacaksın."
# X değerini hesapla.
yasim = int(input("kaç yaşındasın? "))
print(f"10 yıl sonra {yasim + 10} yaşında olacaksın.")

# --- BÖLÜM 3: Ondalıklı sayı ---

# TODO 3: Kullanıcıdan boyunu al (örnek: 1.75).
# float() ile sayıya çevir.
# Sonra şunu yazdır:
# "Boyun X metre."
boyum = float(input("boyun kaç metre? "))
print(f"boyun {boyum} metre.")
# --- BÖLÜM 4: Mini form ---

# TODO 4: Kullanıcıdan şu 3 bilgiyi sırayla al:
# - Ad
# - Yaş (int)
# - Favori renk
#
# Sonra şunu yazdır:
# -------------------
# Ad: Ahmet
# Yaş: 17
# Favori renk: mavi
# -------------------
# (Çizgi çizgiler sabit, bilgiler değişkenden gelmeli.)

isim = input("Adın ne? ")
yasim = int(input("kaç yaşındasın? "))
renk = input("favori rengin ne? ")
print("-------------------")
print(f"Ad: {isim}")
print(f"Yaş: {yasim}")
print(f"Favori renk: {renk}")
print("-------------------")
# --- BÖLÜM 5: Basit hesap makinesi ---

# TODO 5: Kullanıcıdan iki sayı al.
# İkisini topla ve sonucu yazdır:
# "12 + 8 = 20"  gibi.
# Sayıları int() ile çevir.

sayi1 = int(input("Birinci sayı: "))
sayi2 = int(input("ikinci sayı: "))
print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
# --- BONUS ---
# input() çağrıldığında kullanıcı hiçbir şey yazmadan
# Enter'a basarsa ne olur?
# Dene ve Claude'a anlat.
