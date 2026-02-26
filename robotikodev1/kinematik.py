import numpy as np
import matplotlib.pyplot as plt

# Robot Kolunun link uzunlukları
L1 = 0.5
L2 = 0.4
L3 = 0.3

# İleri kinematik fonksiyonu: Verilen eklem açılarına göre end-effector pozisyonunu hesaplar
def ileri_kinematik(q1, q2, q3):
    px = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
    py = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
    return px, py

ornek_px, ornek_py = ileri_kinematik(0, np.pi/4, np.pi/2)
print("--- Örnek Hesaplama Sonucu (İleri Kinematik) ---")
print(f"X Pozisyonu: {ornek_px:.3f} metre")
print(f"Y Pozisyonu: {ornek_py:.3f} metre\n")

# Workspace (Çalışma Alanı) Hesaplama
print("Çalışma alanı (Workspace) hesaplanıyor, lütfen bekleyin...")
aci_degerleri = np.linspace(-np.pi, np.pi, 30) 
x_noktalari = []
y_noktalari = []

for q1 in aci_degerleri:
    for q2 in aci_degerleri:
        for q3 in aci_degerleri:
            x, y = ileri_kinematik(q1, q2, q3)
            x_noktalari.append(x)
            y_noktalari.append(y)

# Ters kinematik fonksiyonu: Verilen hedef pozisyona göre eklem açılarını hesaplar
def ters_kinematik(hedef_x, hedef_y, hedef_z, hedef_phi):
    print(f"\n--- Ters Kinematik (IK) Hedefi: (X:{hedef_x}, Y:{hedef_y}, Z:{hedef_z}) ---")
    
    # 1. Z ekseninin 0 olup olmadığını kontrol etmek
    if hedef_z != 0:
        print("HATA: Çözüm Yok")
        print("Neden: RRR Planar kol sadece XY düzleminde (Z=0) hareket edebilir.")
        print("Z ekseni 0 olmadığı için bu noktaya fiziksel olarak ulaşılamaz.\n")
        return None
        
    pwx = hedef_x - L3 * np.cos(hedef_phi)
    pwy = hedef_y - L3 * np.sin(hedef_phi)
    
    cos_q2 = (pwx**2 + pwy**2 - L1**2 - L2**2) / (2 * L1 * L2)
    
    if cos_q2 > 1 or cos_q2 < -1:
        print("Hedef nokta robotun uzanabileceği alanın dışında.\n")
        return None
        
    q2 = np.arccos(cos_q2)
    
    k1 = L1 + L2 * np.cos(q2)
    k2 = L2 * np.sin(q2)
    q1 = np.arctan2(pwy, pwx) - np.arctan2(k2, k1)
    q3 = hedef_phi - q1 - q2
    
    print("Çözüm Bulundu (Dirsek Aşağı):")
    print(f"q1 = {np.degrees(q1):.2f} derece")
    print(f"q2 = {np.degrees(q2):.2f} derece")
    print(f"q3 = {np.degrees(q3):.2f} derece\n")
    return q1, q2, q3

# Çizimi ekranda göster
plt.figure(figsize=(7, 7))
plt.scatter(x_noktalari, y_noktalari, s=1, c='blue', alpha=0.3)
plt.title('3-DoF RRR Planar Robot Calisma Alani')
plt.xlabel('X Ekseni (Metre)')
plt.ylabel('Y Ekseni (Metre)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.axis('equal')
plt.show()


ters_kinematik(hedef_x=0.8, hedef_y=0.2, hedef_z=0.1, hedef_phi=0.0)
ters_kinematik(hedef_x=0.5, hedef_y=0.5, hedef_z=0.0, hedef_phi=np.pi/4)

