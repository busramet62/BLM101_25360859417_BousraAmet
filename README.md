## BLM101_25360859417_BousraAmet
# TEMEL MANTIK DEVRE SİMÜLATÖRÜ 
Öğrenci Bilgileri: 
* İsim : Bousra
* Soyisim : AMET
* Öğrenci no : 25360859417
* Proje Konusu: 3. Grup- Veri Manipülasyonu ve Mantık Kapıları
* Youtube Video Linki: <https://www.youtube.com/watch?v=1DJnXelpsaI>

### Projenin özeti :
Bu Python projesi, temel mantık kapılarını (AND, OR, NOT, XOR, NAND, NOR) simüle eden ve kullanıcı çıkış yapana kadar sürekli çalışan interaktif bir terminal uygulamasıdır. Program iki temel işlev sunar: İlk olarak, kullanıcının seçtiği belirli bir mantık kapısı için girilen 0 veya 1 değerlerine göre anlık işlem sonucu üretir; ikinci olarak ise üç değişkenli (A, B, C) daha karmaşık mantık devreleri için işlem önceliğini (parantez yerini) dikkate alarak tüm olası giriş kombinasyonlarını hesaplayıp detaylı bir doğruluk tablosu oluşturur. Kod yapısı, iç içe döngüler ve koşullu ifadeler kullanarak Boolean cebiri mantığını pratik bir şekilde kodlamayı amaçlar.

### Özellikler

Bu simülatör kullanıcılara 3 temel seçenek sunar:

1.  **Tekil Kapı Hesaplama:** * Kullanıcıdan alınan giriş değerlerine (0 veya 1) göre seçilen kapının sonucunu anlık olarak hesaplar.
    * Desteklenen kapılar: `AND`, `OR`, `NOT`(Sadece 1. hesaplamada), `XOR`, `NAND`, `NOR`.
2.  **Doğruluk Tablosu Oluşturma:** * 3 değişkenli (A, B, C) devrelerin tüm olasılıklarını (000'dan 111'e kadar) hesaplar.
    * İşlem önceliği seçimi (Parantez içi öncelik veya soldan sağa işlem) sunar.
3.  **Dinamik Menü:** * `while` döngüsü ile program sürekli çalışır, kullanıcı "Çıkış" (3 sayısı girene kadar) diyene kadar yeni hesaplamalar yapılabilir.

### Kurulum ve Çalıştırma

Bu projeyi bilgisayarınızda çalıştırmak için Python'un yüklü olması gerekir.

1.  Projeyi bilgisayarınıza indirin (veya bu repoyu klonlayıp) visual studio veya herhangi bir python dili uygulamasında çalıştırın.

2.  Visual studio veya herhangi bir python dili çalıştıran uygulama indirin ya da online bir compiler kullanınız.

3.  Kopyaladığınız veya indirdiğiniz bu kodları oraya yapıştırın ardından RUN ettiğinizde programınız çalışacaktır.

### Kullanım Örnekleri

#### 1. Mantık Kapısı Hesaplama
Kullanıcı AND kapısını seçip 1 ve 0 değerlerini girdiğinde:

--- Mantık Kapısı Hesaplama ---
Kapı türü: AND
1. Giriş: 1
2. Giriş: 0

Sonuç (AND): 0

#### 2. Doğruluk Tablosu oluşturma
Kullanıcı (A AND B) OR C işlemini seçtiğinde sırasıyla tüm ihtimaller bir tablo olarak ekrana yansıtılıyor. (Parantez yerini de kullanıcıdan alarak başta veya sonda olarak ayarlayıp ona göre farklı sonuçlar alırız).
İşlemdeki AND OR NAND gibi kapılar da kullanıcıdan alınıp hesaplama yapılıyor.

#### 3. Çıkış
Kullanıcı 3 sayısını girdiğinde program sonlanır.
