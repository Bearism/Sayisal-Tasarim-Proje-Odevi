def uarayuz2():
    print("""
    **************************************
    Biriminiz hangi birime dönüştürülecek?
    **************************************
    
    1.Kilometre
    2.Hektometre
    3.Dekametre
    4.Metre
    5.Desimetre
    6.Santimetre
    7.Milimetre
    8.Inch
    9.Feet
    10.Mil
    11.Yard
    0.Çıkış                     
    """)
    
def uzunluk(x,metre):
    if(x == 8):
        
        sonuc = metre * 39.37
        return (str(sonuc) +" inch'e eşittir")
        
    elif(x == 9):
        
        sonuc = metre * 3.28
        return (str(sonuc) +" feet'e eşittir")
        
    elif(x == 10):
        
        sonuc = metre * 0.00062
        return (str(sonuc) +" mil'e eşittir")
        
    elif(x == 11):
        
        sonuc = metre * 1.093
        return (str(sonuc) +" yard'a eşittir")

yanıtuz = {1: lambda :"Kilometre",
         2: lambda :"Hektometre",
         3: lambda :"Dekametre",
         4: lambda :"Metre",
         5: lambda :"Desimetre",
         6: lambda :"Santimetre",
         7: lambda :"Milimetre",
         8: lambda :"Inch",
         9: lambda :"Feet",
         10: lambda :"Mil",
         11: lambda :"Yard"}

def uzhesapla2(h):
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0;
    u2 = float(input(yanıtuz[h]()+":"))
    cevrim = {8: lambda : 39.37,
              9: lambda : 3.28,
              10: lambda : 0.00062,
              11: lambda : 1.093}
    metre = u2 / cevrim[h]()
    sonuc = metre * (10**(c-4))
    if(c < 8):
        print(str(u2)+" "+ yanıtuz[h]()+" "+ str(sonuc)+" "+ yanıtuz[c]()+"'ye eşittir")
    elif(c >= 8):
        print(str(u2)+" "+ yanıtuz[h]()+" "+ uzunluk(c,metre))
def uzhesapla(h):
    
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))            
    u1 = float(input(yanıtuz[h]()+":"))
    metre = u1 * (10**(h-4))
    if(c < 8):
        
        sonuc = u1 * (10**(c-h))
        print(str(u1) +" "+ yanıtuz[h]() +" "+ str(sonuc) +" "+ yanıtuz[c]()+"'ye eşittir")
        
    elif(c <= 11):
        
        print(str(u1) +" "+ yanıtuz[h]()+" "+ uzunluk(c,metre))
    
    else:
        print("Gireceğiniz sayı 1 ile 11 arasında olmalıdır")
        uzhesapla(h)

def karayuz2():
    print("""
    **************************************
    Biriminiz hangi birime dönüştürülecek?
    **************************************     
    
    1.Ton
    2.Kilogram
    3.Gram
    4.Miligram
    5.Pound
    6.Ounce
    0.**Geri**
    
    """)

yanıtkütle = {1: lambda :"Ton",
              2: lambda :"Kilogram",
              3: lambda :"Gram",
              4: lambda :"Miligram",
              5: lambda :"Pound",
              6: lambda :"Ounce"}

def khesapla(h):
    
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0;
    k1 = float(input(yanıtkütle[h]()+":"))
    if(c < 5):
        sonuc = k1 * (10**(3*c-3*h))
        print(str(k1) +" "+ yanıtkütle[h]() +" "+ str(sonuc) +" "+ yanıtkütle[c]()+"'a eşittir")
    elif (c == 5 or c == 6):
        cevrim = {5: lambda : 0.002204,
                  6: lambda : 0.0352}
        gram = k1 * (10**(-(h-3)*3))
        sonuc = gram * (cevrim[c]())
        print(str(k1) +" "+ yanıtkütle[h]() +" "+ str(sonuc) +" "+ yanıtkütle[c]()+"'a eşittir")
    else:
        print("Gireceğiniz sayı 1 ile 6 arasında olmalıdır")
        khesapla(h)
        
def khesapla2(h):
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0
    k1 = float(input(yanıtkütle[h]()+":"))
    cevrim = {5: lambda : 0.002204,
              6: lambda : 0.0352}
    gram = k1 / cevrim[h]()
    if(c < 5):
        sonuc = gram * (10**(3*(c-3)))
        print(str(k1) +" "+ yanıtkütle[h]() +" "+ str(sonuc) +" "+ yanıtkütle[c]()+"'a eşittir")
    if(5 <= c < 7):
        sonuc = gram * cevrim[c]()
        print(str(k1) +" "+ yanıtkütle[h]() +" "+ str(sonuc) +" "+ yanıtkütle[c]()+"'a eşittir")
    else:
        print("Gireceğiniz sayı 1 ile 6 arasında olmalıdır")
        khesapla2(h)
        
def zarayuz2():
    print("""
    **************************************
    Biriminiz hangi birime dönüştürülecek?
    **************************************     
    
    1.Asır(Yüzyıl)
    2.Yıl
    3.Ay
    4.Hafta
    5.Gün
    6.Saat
    7.Dakika
    8.Saniye
    9.Salise
    10.Milisaniye
    0.**Geri**
    """)
    
yanıtzaman = {1: lambda :"Asır",
              2: lambda :"Yıl",
              3: lambda :"Ay",
              4: lambda :"Hafta",
              5: lambda :"Gün",
              6: lambda :"Saat",
              7: lambda :"Dakika",
              8: lambda :"Saniye",
              9: lambda :"Salise",
              10: lambda :"Milisaniye"}
    
def zhesapla(h):
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0
    if(1 <= c <= 10):
        z1 = float(input(yanıtzaman[h]()+":"))
        zkatsayı = {10: lambda :86400000,
                    9: lambda :5184000,
                    8: lambda :86400,
                    7: lambda :1440,
                    6: lambda :24,
                    5: lambda :1,
                    4: lambda :0.142857143,
                    3: lambda :0.0328549112,
                    2: lambda :0.00273790926,
                    1: lambda :0.0000273790926}
        gun = z1 / zkatsayı[h]()
        sonuc = gun * zkatsayı[c]()
        ekler = {10: lambda :"ye",
                    9: lambda :"ye",
                    8: lambda :"ye",
                    7: lambda :"ya",
                    6: lambda :"e",
                    5: lambda :"e",
                    4: lambda :"ya",
                    3: lambda :"a",
                    2: lambda :"a",
                    1: lambda :"a"}
        print(str(z1) +" "+ yanıtzaman[h]() +" "+ str(round(sonuc,3)) +" "+ yanıtzaman[c]()+"'{} eşittir".format(ekler[c]()))
    else:
        print("Gireceğiniz sayı 1 ile 10 arasında olmalıdır")
        zhesapla(h)
    
def sarayuz2():
    print("""
    **************************************
    Biriminiz hangi birime dönüştürülecek?
    **************************************      
      
    1.Celsius
    2.Fahrenheit
    3.Kelvin
    4.Reaumur
    0.**Geri**               
    """)
    
yanıtsıcak = {1: lambda :"Celsius",
              2: lambda :"Fahrenheit",
              3: lambda :"Kelvin",
              4: lambda :"Reaumur"}
    
def shesapla(h):
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0
    s1 = float(input(yanıtsıcak[h]()+":"))
    if(c == h):
        sonuc = s1
    if(c == 1 and h == 2):
        sonuc = (s1 - 32)/1.8
    if(c == 1 and h == 3):
        sonuc = s1 + 273.15
    if(c == 1 and h == 4):
        sonuc = s1 / 1.25
    if(c == 2 and h == 1):
        sonuc = (s1 * 1.8)+32
    if(c == 2 and h == 3):
        sonuc = ((s1 + 273.15)*1.8)-32
    if(c == 2 and h == 4):
        sonuc = ((s1 / 1.25)*1.8)-32
    if(c == 3 and h == 1):
        sonuc = s1 - 273.15
    if(c == 3 and h == 2):
        sonuc = ((s1-32)/1.8)-273.15
    if(c == 3 and h == 4):
        sonuc = (s1 / 1.25)-273.15   
    if(c == 4 and h == 1):
        sonuc = s1 * 1.25
    if(c == 4 and h == 2):
        sonuc = ((s1-32)/1.8)*1.25
    if(c == 4 and h == 3):
        sonuc = (s1 + 273.15)*1.25
    else:
        print("Gireceğiniz sayı 1 ile 4 arasında olmalıdır")
        shesapla(h)
        
    print(str(s1) +" "+ yanıtsıcak[h]() +" "+ str(sonuc) +" "+ yanıtsıcak[c]()+"'a eşittir")
 
def darayuz2():
    print("""
    **************************************
    Biriminiz hangi birime dönüştürülecek?
    **************************************      
      
    1.Kilobirim
    2.Hektobirim
    3.Dekabirim
    4.Birim
    5.Desibirim
    6.Santibirim
    7.Milibirim
    0.**Geri**               
    """)
    
yanıtdiger = {1: lambda :"Kilobirim",
         2: lambda :"Hektobirim",
         3: lambda :"Dekabirim",
         4: lambda :"Birim",
         5: lambda :"Desibirim",
         6: lambda :"Santibirim",
         7: lambda :"Milibirim"}

def dhesapla(h):
    c = int(input("Elde etmek istediğiniz birimi seçiniz:"))
    if(c == 0):
        return 0
    if(1 <= c <= 7):
        d1 = float(input(yanıtdiger[h]()+":"))
        sonuc = d1 * (10**(c-h))
        print(str(d1) +" "+ yanıtdiger[h]() +" "+ str(sonuc) +" "+ yanıtdiger[c]()+"'e eşittir")
    else:
        print("Gireceğiniz sayı 1 ile 7 arasında olmalıdır")
        dhesapla(h)
        
while True:
    print("""
    ***********************************************
    Acayip Kapsamlı Birim Dönüştürücüye Hoşgeldiniz
    ***********************************************
    
    
    Dönüştürmek istediğiniz birimin türünü seçiniz..
    
    1.Uzunluk
    2.Kütle
    3.Zaman
    4.Sıcaklık
    5.Deka,kilo,mega içeren diğer birimler
    0.Programdan Çıkış
    
    """)
    a = input("Birim türü seçiniz:")
    if(a == "0"):
        print("Uygulama sonlandırılıyor...")
        break
    while True:
        if(a == "1"):
            print("""
    **************************************
    Dönüştürmek istediğiniz birimi seçiniz
    **************************************
    
    1.Metre
    2.Milimetre
    3.Santimetre
    4.Desimetre
    5.Dekametre
    6.Hektometre
    7.Kilometre
    8.Inch
    9.Feet
    10.Mil
    11.Yard
    0.**Geri**
    
            """)
            b = int(input("Elinizdeki birimi seçiniz:"))
            if(b == 0):
                break
                
            if(b == 1):
                uarayuz2()
                uzhesapla(4)
                    
            if(b == 2):
                uarayuz2()
                uzhesapla(7)
                    
            if(b == 3):
                uarayuz2()
                uzhesapla(6)
                    
            if(b == 3):
                uarayuz2()
                uzhesapla(5)
                
            if(b == 5):
                uarayuz2()
                uzhesapla(3)
    
            if(b == 6):
                uarayuz2()
                uzhesapla(2)
                                    
            if(b == 7):
                uarayuz2()
                uzhesapla(1)
            if(b <= 11):
                uarayuz2()
                uzhesapla2(b)
            else:
                print("1 ile 11 arasında bir sayı giriniz")
                continue
                
                
        elif(a == "2"):
            print("""
    **************************************
    Dönüştürmek istediğiniz birimi seçiniz
    **************************************
    
    1.Ton
    2.Kilogram
    3.Gram
    4.Miligram
    5.Pound
    6.Ounce
    0.**Geri**
            """)
            b = int(input("Elinizdeki birimi seçiniz:"))
            if(b == 0):
                break
            if(1 <= b < 5):
                karayuz2()
                khesapla(b)
            elif(5 <= b < 7):
                karayuz2()
                khesapla2(b)
            else:
                print("1 ile 6 arasında bir sayı giriniz")
                continue
            
        elif(a == "3"):
            print("""
    **************************************
    Dönüştürmek istediğiniz birimi seçiniz
    **************************************  
    
    1.Asır(Yüzyıl)
    2.Yıl
    3.Ay
    4.Hafta
    5.Gün
    6.Saat
    7.Dakika
    8.Saniye
    9.Salise
    10.Milisaniye
    0.**Geri**
            """)
            b = int(input("Elinizdeki birimi seçiniz:"))
            if(b == 0):
                break
            if(1 <= b < 11):
                zarayuz2()
                zhesapla(b)
            else:
                print("1 ile 11 arasında bir sayı giriniz")
                continue
            
        elif(a == "4"):
            print("""
    **************************************
    Dönüştürmek istediğiniz birimi seçiniz
    **************************************
                  
    1.Celsius
    2.Fahrenheit
    3.Kelvin
    4.Reaumur                 
    0.**Geri**                         
            """)
            b = int(input("Elinizdeki birimi seçiniz:"))
            if(b == 0):
                break
            if(1 <= b <= 4):
                sarayuz2()
                shesapla(b)
            else:
                print("1 ile 4 arasında bir sayı giriniz")
                continue
        elif(a == "5"):
            print("""
    **************************************
    Dönüştürmek istediğiniz birimi seçiniz
    **************************************
                  
    1.Kilobirim
    2.Hektobirim
    3.Dekabirim
    4.Birim
    5.Desibirim
    6.Santibirim
    7.Milibirim
    0.**Geri**
            """)
            b = int(input("Elinizdeki birimi seçiniz:"))
            if(b == 0):
                break
            if(1 <= b <= 7):
                darayuz2()
                dhesapla(b)
        
        else:
            print("Gireceğiniz sayı 1 ile 5 arasında olmalıdır")
            continue