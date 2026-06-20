# =============================================================================
# KOD-ASİSTAN PROJESİ v0.3 - DÖNGÜ KONTROLLÜ TAHMİN OYUNU MODÜLÜ
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / while, break ve continue Komutlarının Entegrasyonu
# =============================================================================

import random

print("=== KOD-ASİSTAN: SAYI TAHMİN OYUNU MODÜLÜ AKTİF ===")
print("Sistem 1 ile 50 arasında gizli bir sayı belirledi. Bulmak için 5 hakkınız var!\n")

# 1. AŞAMA: Oyun parametrelerinin ve gizli sayının bellekte hazırlanması
gizli_sayi = random.randint(1, 50)
kalan_hak = 5
tahmin_sayaci = 0

# 2. AŞAMA: Oyun Döngüsünün Başlatılması
while kalan_hak > 0:
    girdi = input(f"Kalan Hakkınız ({kalan_hak}). Tahmininizi giriniz: ").strip()
    tahmin = int(girdi)
    
    # DBF KAZANIMI: GEÇERSİZ ARALIK GİRİŞİNİN "CONTINUE" İLE ATLANMASI
    if tahmin < 1 or tahmin > 50:
        print("🚨 Uyarı: Tahmininiz 1 ile 50 arasında olmalıdır!")
        print("Sistem kararlılığını korumak için bu adım atlanıyor ve hakkınız eksilmiyor.\n")
        # KONTROL İFADESİ: Aşağıdaki kodları çalıştırmadan doğrudan döngü koşuluna döner.
        continue
    
    # Geçerli bir tahmin yapıldığı için sayaçları güncelleme adımı
    tahmin_sayaci += 1
    kalan_hak -= 1
    
    # 3. AŞAMA: ÇOK KRİTERLİ DOĞRULAMA VE DÖNGÜ YÖNETİMİ
    if tahmin == gizli_sayi:
        print(f"\n🎉 Tebrikler! Gizli sayıyı {tahmin_sayaci}. denemenizde buldunuz.")
        # KONTROL İFADESİ: Koşulun hala hakkı olmasına bakılmaksızın döngüyü anında kırar.
        break
        
    elif tahmin > gizli_sayi:
        print("❌ İpucu: Daha KÜÇÜK bir sayı girmelisiniz.\n")
        
    else:
        print("❌ İpucu: Daha BÜYÜK bir sayı girmelisiniz.\n")

# 4. AŞAMA: Oyun Sonu Durum Kontrolü
if kalan_hak == 0 and tahmin != gizli_sayi:
    print("\n😔 Maalesef tahmin hakkınız bitti ve oyun sonlandı.")
    print(f"Sistemin belirlediği gizli sayı: {gizli_sayi} idi. Bir sonraki sefere başarılar!")

print("\n=== OYUN MODÜLÜ KAPATILDI ===")
