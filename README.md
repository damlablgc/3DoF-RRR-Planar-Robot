# 3-DoF RRR Planar Robot Manipülatörü: Kinematik Analiz ve Simülasyon

Bu proje, 3 Serbestlik Dereceli (3-DoF) RRR (Revolute-Revolute-Revolute) planar bir robot kolunun ileri/ters kinematik analizini, çalışma alanı (workspace) görselleştirmesini ve Gazebo ortamında fiziksel simülasyonunu içermektedir.

## 🤖 Robot Seçimi ve Konfigürasyon
Projede XY düzleminde hareket eden **RRR Planar Kol** konfigürasyonu seçilmiştir.
- **Link Uzunlukları:** L1 = 0.5m, L2 = 0.4m, L3 = 0.3m
- **Mafsal Limitleri:** q_i ∈ [-π, π] (Serbest dönüş)

## 📂 Depo İçeriği
- `kinematik.py`: İleri/Ters kinematik hesaplamalarını ve çalışma alanı görselleştirmesini yapan Python kodu.
- `robot.sdf`: Gazebo simülasyonu için fizik, çarpışma ve görsel özellikleri tanımlanmış model dosyası.

## 🚀 Çalıştırma Talimatları

### 1. Kinematik Analiz (Python)
Gerekli kütüphaneleri yükleyin ve Python dosyasını çalıştırın:
```bash
pip install numpy matplotlib
python kinematik.py
