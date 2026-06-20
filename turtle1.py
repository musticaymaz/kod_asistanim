import turtle

# Grafik penceresini ve çizim kalemini hazırla
kalem = turtle.Turtle()

# VERİMLİ DÖNGÜSEL MODELLEME: Aynı 2 satırı kopyalamak yerine 4 kez döndür
for sayac in range(4):
    kalem.forward(100) # 100 piksel ileri git
    kalem.right(90)    # 90 derece sağa dön (Kare köşesi)

turtle.done() # Çizim bittiğinde pencereyi açık tut