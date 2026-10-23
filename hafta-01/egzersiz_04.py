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


# --- BÖLÜM 2: Sayı alma ---

# TODO 2: Kullanıcıdan yaşını al.
# int() ile sayıya çevir.
# Sonra şunu yazdır:
# "10 yıl sonra X yaşında olacaksın."
# X değerini hesapla.


# --- BÖLÜM 3: Ondalıklı sayı ---

# TODO 3: Kullanıcıdan boyunu al (örnek: 1.75).
# float() ile sayıya çevir.
# Sonra şunu yazdır:
# "Boyun X metre."


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


# --- BÖLÜM 5: Basit hesap makinesi ---

# TODO 5: Kullanıcıdan iki sayı al.
# İkisini topla ve sonucu yazdır:
# "12 + 8 = 20"  gibi.
# Sayıları int() ile çevir.


# --- BONUS ---
# input() çağrıldığında kullanıcı hiçbir şey yazmadan
# Enter'a basarsa ne olur?
# Dene ve Claude'a anlat.
