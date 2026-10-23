# ============================================================
# HAFTA 1 — EGZERSİZ 3
# Konu: F-string ve string birleştirme
# Süre: ~25 dakika
# ============================================================
#
# F-STRING NEDİR?
# Değişkenin değerini doğrudan yazının içine koymana yarar.
#
# Eski yol (zor):
#   print("Merhaba " + isim + "!")
#
# F-string (kolay):
#   print(f"Merhaba {isim}!")
#
# Kurallar:
#   - Tırnaktan önce f harfi yaz.
#   - Değişkeni süslü parantez {} içine koy.
# ============================================================


# --- BÖLÜM 1: F-string temeli ---

isim = "Zeynep"
yas = 17
sehir = "İstanbul"

# Bu satır zaten çalışıyor:
print(f"Merhaba, benim adım {isim}.")

# TODO 1: f-string kullanarak şunu yazdır:
# "Zeynep 17 yaşında ve İstanbul'da yaşıyor."
# Değişkenleri kullan, metni elle yazma.


# --- BÖLÜM 2: Sayı ile f-string ---

boy = 1.75
kilo = 68

# TODO 2: f-string kullanarak şunu yazdır:
# "Boyum 1.75 metre, kilom 68 kg."


# --- BÖLÜM 3: Hesaplama içinde f-string ---

# f-string içinde doğrudan işlem yapabilirsin.
# Örnek:
print(f"İki kere üç: {2 * 3}")

# TODO 3: f-string kullanarak şunu yazdır:
# "5 yıl sonra 22 yaşında olacağım."
# 22 sayısını elle yazma. yas + 5 kullan.


# --- BÖLÜM 4: Birden fazla değişken ---

ders = "Python"
hafta = 1
egzersiz = 3

# TODO 4: f-string kullanarak şunu yazdır:
# "Python dersinin 1. haftasında, 3. egzersizini çözüyorum."
# Değişkenleri kullan.


# --- BÖLÜM 5: Kendi cümlen ---

# TODO 5: isim, yas, sehir değişkenlerini kendi bilgilerinle güncelle.
# Sonra bir cümle yaz. İstediğin cümleyi yazabilirsin.
isim = "..."    # buraya kendi adını yaz
yas = 0         # buraya kendi yaşını yaz
sehir = "..."   # buraya kendi şehrini yaz

# TODO 5 devam: f-string ile bir tanıtım cümlesi yazdır.


# --- BONUS ---
# f-string içine ne koyarsan ne olur dene:
# {yas * 2}
# {isim.upper()}
# {len(isim)}
# Sonuçları Claude'a anlat.
