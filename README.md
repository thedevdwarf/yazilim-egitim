# Yazılım Eğitim

17 yaşında bir öğrenci için evde yazılım eğitimi. Claude Code ile interaktif çalışıyor.

## Nasıl çalışır?

Öğrenci her seansta bu klasörü Claude Code'da açar. Claude, `CLAUDE.md`'deki tutor talimatlarını okur ve `progress.md`'ye bakarak kaldığı yerden devam eder.

```bash
cd yazilim-egitim
claude
```

Claude soruları direkt cevaplamaz — önce soru sorar, ipucu verir, öğrencinin kendisi bulsun ister.

## Müfredat

| Hafta | Konu | Durum |
|-------|------|-------|
| 1 | print(), değişkenler, f-string, input() | ✅ Hazır |
| 2 | if/elif/else, karşılaştırma | 🔜 |
| 3 | for ve while döngüleri | 🔜 |
| 4 | Listeler ve sözlükler | 🔜 |
| 5 | Fonksiyonlar | 🔜 |
| 6 | Dosya işlemleri, try/except | 🔜 |
| 7 | OOP temelleri | 🔜 |
| 8 | Git ve GitHub | 🔜 |
| 9–11 | Algoritmalar | 🔜 |
| 12 | Final projesi | 🔜 |

## Repo yapısı

```
yazilim-egitim/
├── CLAUDE.md         # Claude'un tutor talimatları
├── progress.md       # İlerleme takibi
└── hafta-01/
    ├── README.md
    ├── egzersiz_01.py   # print() ve yorumlar
    ├── egzersiz_02.py   # Değişkenler
    ├── egzersiz_03.py   # F-string
    ├── egzersiz_04.py   # input()
    └── egzersiz_05.py   # Mini meydan okuma
```

## İlerleme

`progress.md` dosyasına bakın.
