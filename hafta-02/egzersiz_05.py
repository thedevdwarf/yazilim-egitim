# ============================================================
# HAFTA 2 — EGZERSİZ 5
# Konu: Mini meydan okuma — karar verme
# Süre: ~45 dakika
# ============================================================
#
# Bu egzersizde bu haftanın tüm konularını kullanacaksın:
#   if / else   → iki seçenek
#   elif        → çok seçenek
#   and, or, not → birden fazla koşul
#   iç içe if   → adım adım karar
#
# Bu egzersizde ipucu daha az. Takılırsan Claude'a sor.
# ============================================================


# ============================================================
# GÖREV 1: Beden hesaplayıcı
# ============================================================
# Kullanıcıdan boy (cm, int) ve kilo (kg, float) al.
# Vücut kitle indeksini hesapla: VKİ = kilo / (boy/100)²
#
# Sonucu şu tabloya göre değerlendir:
#   VKİ < 18.5          → "Zayıf"
#   18.5 ≤ VKİ < 25.0   → "Normal"
#   25.0 ≤ VKİ < 30.0   → "Fazla kilolu"
#   VKİ ≥ 30.0          → "Obez"
#
# Örnek çıktı:
#   VKİ: 22.5 → Normal

# Kodunu buraya yaz:


# ============================================================
# GÖREV 2: Basit hesap makinesi (işlem seçimli)
# ============================================================
# Kullanıcıdan iki sayı al (float).
# Sonra işlem seçtir: +, -, *, /
#
# Seçime göre işlemi yap ve sonucu yazdır.
# Bölme seçilirse ve ikinci sayı 0 ise:
#   "Sıfıra bölünemez." yazdır.
# Geçersiz işlem girilirse:
#   "Geçersiz işlem." yazdır.
#
# Örnek çıktı:
#   15.0 / 3.0 = 5.0

# Kodunu buraya yaz:


# ============================================================
# GÖREV 3: Film öneri sistemi
# ============================================================
# Kullanıcıya 3 soru sor:
#   1. Ruh hali: "mutlu", "üzgün" veya "heyecanlı"
#   2. Yalnız mı izleyecek? ("evet" / "hayır")
#   3. Kaç saati var? (int)
#
# Bu koşullara göre film öner:
#
#   mutlu + yalnız + 2 saat ve üstü    → "The Secret Life of Walter Mitty"
#   mutlu + yalnız + 2 saatten az      → "Paddington"
#   mutlu + arkadaşlı                  → "The Grand Budapest Hotel"
#   üzgün + 2 saat ve üstü            → "Up"
#   üzgün + 2 saatten az               → "Soul"
#   heyecanlı + yalnız                 → "Interstellar"
#   heyecanlı + arkadaşlı              → "Mad Max: Fury Road"
#   diğer                              → "İyi seyirler :)"
#
# İpucu: ruh hali kontrolü için and/or kullan.

# Kodunu buraya yaz:


# ============================================================
# TAMAMLANDIĞINDA:
# 1. python egzersiz_05.py ile her görevi test et.
# 2. Hepsi çalışıyorsa Claude'a söyle.
# 3. progress.md'yi güncelle.
# 4. git add . && git commit -m "hafta-02 egzersiz_05 tamamlandı" && git push
# ============================================================
