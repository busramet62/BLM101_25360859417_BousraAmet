# BLM101 --- Sanal Mantık Devresi Simülatörü --- Proje 3

while True: # 3 sayısı girilmediği sürece çalışır
    print("\n---------------------------------------")
    print("SANAL MANTIK DEVRESİ SİMÜLATÖRÜ")
    print("1. Mantık Kapısı Hesapla (AND, OR, NOT...)")
    print("2. Doğruluk Tablosu Oluştur (A AND (B OR C))")
    print("3. Çıkış")
    print("---------------------------------------\n")
    
    # Kullanıcıdan işlemi alıyoruz
    secim = input("Yapmak istediğiniz işlemi seçin (1-3): ")

    # 1. 2 Girişli kapoların hesaplanması
    if secim == "1":
        print("\n--- Mantık Kapısı Hesaplama ---")
        print("Kullanabileceğiniz kapılar: AND, OR, NOT, XOR, NAND, NOR")
        kapi_turu = input("Kapı türünü yazınız (Örn: AND): ")
        
       # NOT kapısı (Tek Girişli)
        if kapi_turu == "NOT":
            giris1 = int(input("Giriş değerini giriniz (0 veya 1): "))
            
            # 1 ise 0, 0 ise 1 yapar (ters işlem)
            if giris1 == 1:
                sonuc = 0
            else:
                sonuc = 1
            print("Sonuç (NOT):", sonuc)
        # Bu kapıları ayrı hesaplıyoruz çünkü 2 giriş değeri alır
        elif kapi_turu in ["AND", "OR", "XOR", "NAND", "NOR"]:
            giris1 = int(input("1. Giriş değerini giriniz (0 veya 1): "))
            giris2 = int(input("2. Giriş değerini giriniz (0 veya 1): "))
            sonuc = 0
            
            # AND: Yalnızca ikisi de 1 ise sonuç 1 olur
            if kapi_turu == "AND":
                if giris1 == 1 and giris2 == 1:
                    sonuc = 1
                else:
                    sonuc = 0
            
            # OR: En az biri 1 ise sonuç 1
            elif kapi_turu == "OR":
                if giris1 == 1 or giris2 == 1:
                    sonuc = 1
                else:
                    sonuc = 0
            
            # XOR: Girişler birbirinden FARKLI ise sonuç 1 olur
            elif kapi_turu == "XOR":
                if giris1 != giris2:
                    sonuc = 1
                else:
                    sonuc = 0
            
            # NAND: AND işleminin tam tersi. İkisi de 1 ise 0, diğer durumlarda 1 sonucu yazdırır
            elif kapi_turu == "NAND":
                if giris1 == 1 and giris2 == 1:
                    sonuc = 0
                else:
                    sonuc = 1
            
            # NOR: OR işleminin tam tersi. İkisi de 0 ise 1, diğer durumlarda 0 sonucu döner
            elif kapi_turu == "NOR":
                if giris1 == 0 and giris2 == 0:
                    sonuc = 1
                else:
                    sonuc = 0
            print("\nSonuç (", kapi_turu, "):", sonuc)
        else:
            print("HATA: Geçersiz bir kapı ismi yazdınız! Lütfen listeyi kontrol edin.")

    # 2. DOĞRULUK TABLOSU (Her işlemin değerlerinin alt alta tablosu)
    elif secim == "2":
        print("\n--- Adım 2: Devre Tasarımı ---")
        print("İşlem sırasını (parantez yerini) seçiniz:")
        print("1. (A işlem B) işlem C VEYA A işlem B işlem C  -> [Soldan Sağa / Parantez Başta] VEYA parantezsiz") #Parantez başta olunca da parantez hiç olmayınca da işlemler soldan başlar 
        print("2. A işlem (B işlem C)   -> [Sağdan Sola / Parantez Sonda]")
        yapi_sec = input("Yapı Seçimi (1 veya 2): ")

        # Hangi kapıları kullanacağını alalım
        print("Kullanabileceğiniz kapılar: AND, OR, XOR, NAND, NOR")
        kapi1 = input("1. İşlem Kapısı (Örn: AND): ")
        kapi2 = input("2. İşlem Kapısı (Örn: OR): ")
        
        print("\nDOĞRULUK TABLOSU HESAPLANIYOR...")
        print("A   B   C   |   ARA SONUÇ   |   ANA SONUÇ") # Ara sonuç = Parantezin içindeki işlem, Ana sonuç = Tüm işlemin nihai sonucu
        print("-----------------------------------------")

        # Tüm ihtimaller (0 ve 1) için döngüler
        # 3 farklı sayı olduğundan 3 farklı döngüye ihtiyacımız var
        for a in [0, 1]:
            for b in [0, 1]:
                for c in [0, 1]:
                    
                    # Yapı 1: (A ve B) sonra C
                    if yapi_sec == "1":
                        # Önce parantez içi (A ile B)
                        ara_sonuc = 0
                        if kapi1 == "AND":
                            if a == 1 and b == 1: ara_sonuc = 1
                        elif kapi1 == "OR":
                            if a == 1 or b == 1: ara_sonuc = 1
                        elif kapi1 == "XOR":
                            if a != b: ara_sonuc = 1
                        elif kapi1 == "NAND":
                            if not(a == 1 and b == 1): ara_sonuc = 1
                        elif kapi1 == "NOR":
                            if not(a == 1 or b == 1): ara_sonuc = 1
                        
                        # Sonra ana sonuç (ara_sonuc ile C)
                        ana_sonuc = 0
                        if kapi2 == "AND":
                            if ara_sonuc == 1 and c == 1: ana_sonuc = 1
                        elif kapi2 == "OR":
                            if ara_sonuc == 1 or c == 1: ana_sonuc = 1
                        elif kapi2 == "XOR":
                            if ara_sonuc != c: ana_sonuc = 1
                        elif kapi2 == "NAND":
                            if not(ara_sonuc == 1 and c == 1): ana_sonuc = 1
                        elif kapi2 == "NOR":
                            if not(ara_sonuc == 1 or c == 1): ana_sonuc = 1

                    # Yapı 2: A sonra (B ve C)
                    else:
                        # Önce parantez içi (B ile C)
                        ara_sonuc = 0
                        if kapi1 == "AND":
                            if b == 1 and c == 1: ara_sonuc = 1
                        elif kapi1 == "OR":
                            if b == 1 or c == 1: ara_sonuc = 1
                        elif kapi1 == "XOR":
                            if b != c: ara_sonuc = 1
                        elif kapi1 == "NAND":
                            if not(b == 1 and c == 1): ara_sonuc = 1
                        elif kapi1 == "NOR":
                            if not(b == 1 or c == 1): ara_sonuc = 1
                            
                        # Sonra ana sonuç (A ile ara_sonuc)
                        ana_sonuc = 0
                        if kapi2 == "AND":
                            if a == 1 and ara_sonuc == 1: ana_sonuc = 1
                        elif kapi2 == "OR":
                            if a == 1 or ara_sonuc == 1: ana_sonuc = 1
                        elif kapi2 == "XOR":
                            if a != ara_sonuc: ana_sonuc = 1
                        elif kapi2 == "NAND":
                            if not(a == 1 and ara_sonuc == 1): ana_sonuc = 1
                        elif kapi2 == "NOR":
                            if not(a == 1 or ara_sonuc == 1): ana_sonuc = 1

                    # Sonucu Yazdır
                    print(f"{a}   {b}   {c}   |       {ara_sonuc}         |      {ana_sonuc}") # Düz yazınca simetrik bir görütü oluşturamadım.

    # 3. ÇIKIŞ
    elif secim == "3":
        print("Program kapatılıyor...")
        break # While döngüsünü kırar ve program biter

    # Yanlış seçim yapıldığında (İlk baştan 1,2,3 dışında bir sayı girilirse)
    else:
        print("Lütfen 1, 2 veya 3 seçeneklerinden birini giriniz.")
