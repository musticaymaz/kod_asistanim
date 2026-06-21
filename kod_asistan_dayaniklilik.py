# ==============================================================
# KOD-ASİSTAN PROJESİ v2.0 - İSTİSNA YÖNETİMİ VE DAYANIKLILIK
# Standart: PEP 8 / try-except-finally ve Hata Ayıklama (Debugging)
# ==============================================================

print("=== KOD-ASİSTAN: DAYANIKLI VKİ HESAPLAMA MODÜLÜ ===\n")

while True:
    print("-------------------------------------------------")

    # 1. AŞAMA: Hata Riski Taşıyan Kodların try Bloğuna Alınması
    try:
        girdi = input("Kilonuzu giriniz (Çıkmak için 'q' tuşlayınız): ")

        # Güvenli çıkış protokolü
        if girdi.lower() == 'q':
            print("Sağlıklı günler dileriz! Sistem kapatılıyor...")
            break

        kilo = float(girdi)
        boy = float(input("Boyunuzu metre cinsinden giriniz (Örn: 1.75): "))

        vki = kilo / (boy ** 2)
        print(f"-> Başarılı! Vücut Kitle İndeksiniz: {vki:.2f}")

    # 2. AŞAMA: Kullanıcı Sayı Yerine Harf Girerse Çalışacak except Bloğu
    except ValueError as e:
        print("\n[HATA AĞI] Kritik bir hata yakalandı. Sistem çökmesi engellendi!")
        print(f"Kullanıcı Hatası: Sayısal veri beklenen alana geçersiz karakter girildi.")
        print(f"Log Detayı: {e}\n")
        print("Lütfen verileri doğru formatta yeniden giriniz.")

    # 3. AŞAMA: Her Koşulda Çalışacak Temizlik Bloğu
    finally:
        print("[SİSTEM] VKİ deneme turu tamamlandı ve bellek temizlendi.")