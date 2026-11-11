# ============================================================
# HAFTA 2 — EGZERSİZ 1
# Konu: if / else temeli
# Süre: ~20 dakika
# ============================================================
#
# IF / ELSE NEDİR?
# "Eğer şu koşul doğruysa bunu yap, değilse şunu yap."
#
# Sözdizimi:
#   if koşul:
#       # koşul doğruysa burası çalışır
#   else:
#       # koşul yanlışsa burası çalışır
#
# ÖNEMLİ: if bloğunun içi 4 boşluk girintili olmalı.
# ============================================================


# --- BÖLÜM 1: İlk if / else ---

# Bu örnek zaten çalışıyor, incele:
yas = 15

if yas >= 18:
    print("Ehliyet alabilirsin.")
else:
    print("Henüz ehliyet alamazsın.")

# TODO 1: yas değişkenini 15 yap ve tekrar çalıştır.
# Çıktı değişti mi? Neden?


# --- BÖLÜM 2: Kullanıcıdan al ---

# TODO 2: Kullanıcıdan yaşını al (int() kullan).
# 18 veya üstündeyse "Oy kullanabilirsin." yazdır.
# Değilse "Oy kullanamaya henüz." yazdır.

yas = int(input("Kaç yaşındasın? "))
if yas >= 18:
    print("Oy kullanabilirsin")
else:
    print("Henüz oy kullanamazsınız")

# --- BÖLÜM 3: Sayı karşılaştırma ---

# TODO 3: Kullanıcıdan bir sayı al.
# 0'dan büyükse "Pozitif sayı." yazdır.
# Değilse "Sıfır veya negatif." yazdır.

yas = int(input("Bir sayı yaz "))
if yas > 0:
    print("Positif sayı")
else:
    print("Negatif sayı")


# --- BÖLÜM 4: String karşılaştırma ---

# TODO 4: Kullanıcıdan bir renk al.
# "mavi" yazarsa "Benim de favori rengim!" yazdır.
# Başka bir şey yazarsa "Güzel renk." yazdır.
#
# İpucu: == operatörü eşitlik kontrolü yapar.
# "mavi" == "Mavi" → False  (büyük/küçük harf farklı!)

renk = input ("Favori rengin nedir? ")
if renk == "mavi":
    print ("Benimde favorim!")
else:
    print ("güzel renk!")

# --- BONUS ---
# TODO 4'ü "MAVİ" yazarak test et.
# "mavi" ile eşleşiyor mu?
# Neden? Claude'a anlat.
