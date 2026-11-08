# ============================================================
# HAFTA 2 — EGZERSİZ 2
# Konu: elif zinciri
# Süre: ~25 dakika
# ============================================================
#
# ELIF NEDİR?
# İkiden fazla seçenek olduğunda elif kullanılır.
#
#   if koşul1:
#       ...
#   elif koşul2:
#       ...
#   elif koşul3:
#       ...
#   else:
#       ...
#
# Python yukarıdan aşağı bakar. İlk doğru koşulda durur,
# geri kalanına bakmaz.
# ============================================================


# --- BÖLÜM 1: Harf notu ---

# Bu örneği incele:
puan = 75

if puan >= 90:
    harf = "AA"
elif puan >= 80:
    harf = "BA"
elif puan >= 70:
    harf = "BB"
elif puan >= 60:
    harf = "CB"
else:
    harf = "FF"

print(f"Puanın: {puan} → Harf notun: {harf}")

# TODO 1: puan değişkenini 55, 85, 90 yapıp tekrar çalıştır.
# Her seferinde doğru harf notu çıkıyor mu?


# --- BÖLÜM 2: Kullanıcıdan puan al ---

# TODO 2: Yukarıdaki kodu kullanıcıdan puan alacak şekilde yaz.
# int(input(...)) kullan.
# Aynı harf notu sistemini uygula.


# --- BÖLÜM 3: Hava durumu ---

# TODO 3: Kullanıcıdan sıcaklık al (int).
# 35 ve üstü    → "Çok sıcak, su iç."
# 25–34 arası   → "Güzel hava."
# 15–24 arası   → "Serin, mont al."
# 14 ve altı    → "Soğuk, kalın giy."


# --- BÖLÜM 4: Gün adı ---

# TODO 4: Kullanıcıdan 1–7 arası bir sayı al.
# 1 → "Pazartesi", 2 → "Salı" ... 7 → "Pazar" yazdır.
# 1–7 dışında bir şey girerse "Geçersiz gün." yazdır.


# --- BONUS ---
# elif yerine iç içe if kullansaydık ne olurdu?
# Dene ve Claude'a anlat.
