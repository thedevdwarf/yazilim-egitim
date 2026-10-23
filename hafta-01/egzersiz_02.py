# ============================================================
# HAFTA 1 — EGZERSİZ 2
# Konu: Değişkenler ve veri tipleri
# Süre: ~25 dakika
# ============================================================
#
# DEĞİŞKEN NEDİR?
# Değişken, bir bilgiyi saklamak için kullandığımız isimdir.
# Örnek:
#   isim = "Ahmet"     →  "isim" kutusunda "Ahmet" var
#   yas = 17           →  "yas" kutusunda 17 var
#
# PYTHON'DA 4 TEMEL VERİ TİPİ:
#   str   → Metin.         Örnek: "merhaba"
#   int   → Tam sayı.      Örnek: 42
#   float → Ondalıklı.     Örnek: 1.75
#   bool  → Doğru/Yanlış.  Örnek: True veya False
# ============================================================


# --- BÖLÜM 1: Hazır değişkenler ---

renk = "mavi"
sayi = 42
ondalik = 3.14
dogru_mu = True

print(renk)
print(sayi)

# TODO 1: ondalik ve dogru_mu değişkenlerini de yazdır.


# --- BÖLÜM 2: Kendi değişkenlerini oluştur ---

# TODO 2: Aşağıdaki bilgiler için değişken oluştur ve yazdır.
# Her birinin veri tipini yorum olarak yaz.

# Adın       → str


# Yaşın      → int


# Boyun      → float  (örnek: 1.75)


# Öğrenci misin?  → bool  (True ya da False)


# --- BÖLÜM 3: Değişkeni değiştirme ---

puan = 0
print("Başlangıç puanı:", puan)

# TODO 3: puan değişkenini sırayla değiştir ve her seferinde yazdır.
# 10 yap → yazdır
# 25 yap → yazdır
# 0 yap  → yazdır


# --- BÖLÜM 4: type() fonksiyonu ---

# type() bir değişkenin tipini söyler.
print(type(renk))    # <class 'str'>
print(type(sayi))    # <class 'int'>

# TODO 4: ondalik ve dogru_mu değişkenlerinin tipini yazdır.
# Ne görüyorsun? Claude'a anlat.


# --- BONUS ---
# Bu iki satırı çalıştır. Hata alırsın. Neden olduğunu düşün.
# yasim = "17"
# print(yasim + 1)
