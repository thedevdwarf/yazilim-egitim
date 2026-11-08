# ============================================================
# HAFTA 2 — EGZERSİZ 4
# Konu: İç içe koşullar
# Süre: ~30 dakika
# ============================================================
#
# İÇ İÇE KOŞUL NEDİR?
# Bir if bloğunun içine başka bir if koyabilirsin.
#
#   if dış_koşul:
#       if iç_koşul:
#           ...
#       else:
#           ...
#   else:
#       ...
#
# DİKKAT: Her seviye 4 boşluk daha girintili olmalı.
# Çok derin iç içe yapılar kodu okumayı zorlaştırır.
# Genellikle 2 seviye yeterlidir.
# ============================================================


# --- BÖLÜM 1: Basit iç içe ---

# Bu örneği incele:
uye = True
premium = False

if uye:
    if premium:
        print("Premium içeriklere erişebilirsin.")
    else:
        print("Üyesin ama premium değilsin.")
else:
    print("Önce üye ol.")

# TODO 1: uye = False yap, çalıştır. Hangi mesaj çıktı?
# TODO 2: uye = True, premium = True yap. Şimdi?


# --- BÖLÜM 2: ATM simülasyonu ---

# TODO 3: Basit bir ATM simülasyonu yaz.
# Adım 1: Kullanıcıdan PIN al (doğru PIN: "1234").
# Adım 2: PIN doğruysa kullanıcıdan çekmek istediği miktarı al.
# Adım 3: Bakiye 1000 TL. Miktar bakiyeden az veya eşitse
#         "İşlem tamam. Kalan bakiye: X TL" yazdır.
#         Fazlaysa "Yetersiz bakiye." yazdır.
# Adım 4: PIN yanlışsa "Hatalı PIN." yazdır.


# --- BÖLÜM 3: Mevsim tayini ---

# TODO 4: Kullanıcıdan ay numarası al (1–12).
# Önce geçerli aralıkta mı kontrol et (1–12).
# Geçerliyse mevsimleri yazdır:
#   Aralık, Ocak, Şubat  → Kış
#   Mart, Nisan, Mayıs   → İlkbahar
#   Haziran, Temmuz, Ağustos → Yaz
#   Eylül, Ekim, Kasım   → Sonbahar
# Geçersizse "1–12 arası bir sayı gir." yazdır.


# --- BONUS ---
# ATM simülasyonunu 3 yanlış PIN hakkıyla yaz.
# 3 yanlış girişten sonra "Kart bloke edildi." yazdır.
# İpucu: while döngüsüne henüz girmedik, bunu Claude'a sor.
