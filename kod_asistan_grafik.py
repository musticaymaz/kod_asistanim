# ==============================================================
# KOD-ASİSTAN PROJESİ v0.3 - DÖNGÜSEL GRAFİK VE GEOMETRİ MODÜLÜ
# Geliştirici: [Öğrenci Adı Soyadı]
# Standart: PEP 8 / Disiplinler Arası Matematik ve Döngü Entegrasyonu
# ==============================================================

import turtle

print("=== KOD-ASİSTAN: DÖNGÜSEL GRAFİKSEL GÖRSELLEŞTİRME ===")

# Kullanıcıdan dinamik geometrik veri girişi alınması
kenar_sayisi = int(input("Çizilmesini istediğiniz çokgenin kenar sayısını giriniz (Örn: 3, 5, 6, 8): "))

if kenar_sayisi < 3:
    print("❌ Hata: Bir çokgen oluşturabilmek için en az 3 kenara ihtiyaç vardır!")
else:
    # MATEMATİKSEL MUHAKEME ALANI
    # Geometrik dış açı formülü işlemciye hesaplatılır
    donme_acisi = 360 / kenar_sayisi
    
    print(f"\nHesaplanan Dış Açı: {donme_acisi:.1f} Derece.")
    print("Grafik motoru tetikleniyor, lütfen açılan pencereyi izleyiniz...")
    
    # Çizim kalemi ayarları
    asistan_kalem = turtle.Turtle()
    asistan_kalem.pencolor("purple") # Çizgi rengi
    asistan_kalem.pensize(3)         # Çizgi kalınlığı
    
    # DİNAMİK GRAFİK DÖNGÜSÜ
    # Döngü, kullanıcının girdiği kenar sayısı kadar kusursuzca döner
    for sira in range(kenar_sayisi):
        asistan_kalem.forward(sira*2)             # Her bir kenarın uzunluğu 80 piksel
        asistan_kalem.right(donme_acisi)  # Hesaplanan dinamik açı kadar dönüş
        
    print("✔️ Görselleştirme algoritması başarıyla tamamlandı.")
    turtle.done()
