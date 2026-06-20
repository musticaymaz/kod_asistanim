# =============================================================================
# KOD-ASİSTAN PROJESİ v0.3 - GEOMETRİK BAYRAK SİMÜLASYON MODÜLÜ
# Standart: Türk Bayrağı Kanunu Ölçüleri (G Faktörü) & PEP 8
# =============================================================================

import turtle

# --- Ekran ve Bayrak Ölçek Ayarları ---
G = 300  # Genişlik (Boy = 1.5 * G = 450)
BOY = 1.5 * G

ekran = turtle.Screen()
ekran.setup(width=int(BOY) + 100, height=G + 100)
ekran.bgcolor("#E30A17") # Kanuni Al Kırmızı
ekran.title("Kod-Asistan: Türkiye Bayrağı Simülasyonu")

kalem = turtle.Turtle()
kalem.speed(0)
kalem.hideturtle()

def kusursuz_daire(x, y, yaricap, renk):
    """Yatay eksen doğrultusunda nizami daire çizer."""
    kalem.penup()
    kalem.goto(x, y - yaricap)
    kalem.setheading(0) 
    kalem.pendown()
    kalem.color(renk)
    kalem.begin_fill()
    kalem.circle(yaricap)
    kalem.end_fill()

def kanuni_yildiz_ciz(x, y, R):
    """
    Yıldızın 5 dış ve 5 iç köşesini sırayla birleştirerek
    içi tamamen dolu ve kusursuz geometride beyaz yıldız çizer.
    """
    import math
    
    # İç köşelerin (girintilerin) merkezden uzaklık oranı (Altın Oran)
    r_ic = R * 0.382 
    
    # Yıldızın 10 adet köşe koordinatını (Dış-İç-Dış-İç...) hesaplayıp listeye ekleyelim
    koordinatlar = []
    
    # 0'dan 9'u kadar toplam 10 köşe (Her köşe arası 36 derecedir)
    for i in range(10):
        # Kanuna göre yıldızın tepe noktası sola (hilale) doğru bakmalıdır.
        # Bu yüzden başlangıç açısını 180 derece (Tam Batı) yapıyoruz.
        aci_radyan = math.radians(180 + i * 36)
        
        # Çift endeksler dış köşe, tek endeksler iç köşe
        if i % 2 == 0:
            k_x = x + R * math.cos(aci_radyan)
            k_y = y + R * math.sin(aci_radyan)
        else:
            k_x = x + r_ic * math.cos(aci_radyan)
            k_y = y + r_ic * math.sin(aci_radyan)
            
        koordinatlar.append((k_x, k_y))
    
    # Çizim işlemini başlatma
    kalem.penup()
    kalem.goto(koordinatlar[0]) # İlk dış köşeye git
    kalem.pendown()
    kalem.color("white")
    kalem.begin_fill()
    
    # Tüm koordinatları sırayla çizgiyle birleştir
    for nokta in koordinatlar[1:]:
        kalem.goto(nokta)
        
    kalem.goto(koordinatlar[0]) # Şekli kapatmak için ilk noktaya geri dön
    kalem.end_fill()

# ==========================================
# TÜRK BAYRAĞI KANUNU GEOMETRİK HESAPLAMALARI
# ==========================================

# 1. Dış Daire (M merkezli)
d_merkez_x = -BOY/2 + 0.25 * G + 0.25 * G 
d_merkez_y = 0
d_yaricap = 0.25 * G

# 2. İç Daire (M' merkezli) - Dış merkezden 0.0625 * G kadar sağa kaymış
i_merkez_x = d_merkez_x + 0.0625 * G
i_merkez_y = 0
i_yaricap = 0.2 * G

# 3. Yıldız Çemberi - İç daire merkezinden 0.333 * G kadar sağdadır
y_merkez_x = i_merkez_x + 0.333 * G
y_merkez_y = 0
y_yaricap = 0.125 * G

# ==========================================
# ÇİZİM MOTORUNUN ÇALIŞTIRILMASI
# ==========================================

# 1. Adım: Hilalin dış beyaz gövdesi
kusursuz_daire(d_merkez_x, d_merkez_y, d_yaricap, "white")

# 2. Adım: İç kırmızı daire ile beyaz alanın kesilmesi
kusursuz_daire(i_merkez_x, i_merkez_y, i_yaricap, "#E30A17")

# 3. Adım: İçi tamamen dolu kanuni beyaz yıldız
kanuni_yildiz_ciz(y_merkez_x, y_merkez_y, y_yaricap)

print("✔️ Türkiye Cumhuriyeti Bayrağı kanuni standartlarla eksiksiz şekilde çizildi.")
ekran.exitonclick()