# ============================================================
# HAFTA 2 — EGZERSİZ 3
# Konu: and, or, not operatörleri
# Süre: ~25 dakika
# ============================================================
#
# MANTIKSAL OPERATÖRLER:
#
#   and → İkisi de doğruysa True
#         True  and True  → True
#         True  and False → False
#
#   or  → Biri doğruysa True
#         True  or  False → True
#         False or  False → False
#
#   not → Tersine çevirir
#         not True  → False
#         not False → True
# ============================================================


# --- BÖLÜM 1: and ---

yas = 20
vatandas = True

# İkisi de doğruysa oy kullanabilir:
if yas >= 18 and vatandas:
    print("Oy kullanabilirsin.")
else:
    print("Oy kullanamazsın.")

# TODO 1: vatandas = False yap ve tekrar çalıştır.
# Çıktı değişti mi? Neden?


# --- BÖLÜM 2: or ---

# TODO 2: Kullanıcıdan bir sayı al.
# Sayı 0'dan küçük VEYA 100'den büyükse:
#   "Geçersiz değer. 0–100 arası gir."
# Değilse:
#   "Geçerli değer."


# --- BÖLÜM 3: not ---

# TODO 3: Kullanıcıdan "abone misin?" sorusunu sor.
# "evet" yazarsa "Teşekkürler!" yazdır.
# not kullanarak "evet" dışındaki her şey için
# "Abone olmak ister misin?" yazdır.


# --- BÖLÜM 4: Hepsini bir arada ---

# TODO 4: Bir oyuna giriş sistemi yaz.
# Kullanıcıdan yaşını ve ebeveyn iznini al.
# (ebeveyn izni: "evet" veya "hayır")
#
# Koşullar:
# - 18 yaş ve üstü → direkt girebilir
# - 13–17 arası VE ebeveyn izni "evet" → girebilir
# - 13–17 arası VE ebeveyn izni "hayır" → giremez
# - 12 ve altı → giremez (izin de yetmez)
#
# Her durum için uygun mesaj yazdır.


# --- BONUS ---
# Bu iki satırın sonucu nedir? Tahmin et, sonra çalıştır.
# print(True and False or True)
# print(not False and True)
