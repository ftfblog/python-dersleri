"""

Bu kodlar ftfblog.com tarafından yazılmıştır. 
Bu kodlar ftfblog.com tarafından açık kaynak kodlu olarak paylaşılmaktadır.
Bu kodların yazıldığı yazıya ulaşmak için ftfblog.com/python-dersleri-8-if-else-elif-kosullu-ifadeler

"""

dictionary_degiskeni = {"ad":"ftfblog", "yaş":"1", "yer":"Türkiye"}

dictionary_degiskeni2 = {"ad":"ftfblog",
                        "yaş":"1",
                        "yer":"Türkiye"}
print(dictionary_degiskeni)
print(dictionary_degiskeni2)

dictionary_degiskeni3 = {"ad":"ftfblog",
                        "yas": "1",
                        "yer":{
                               "ilk hedef":"Türkiye",
                               "sonraki hedef":"tüm dünya"
  }
}
print(dictionary_degiskeni3)

dictionary_degiskeni= {
    "ad":"ftfblog",
    "yas":1,
    "yer":{
    "ilk hedef":"Türkiye",
    "sonraki hedef":"tüm dünya"
  }
}

sayı = 10
if sayı > 9:
  print("Sayı 9'dan büyüktür.")


------------------------------


string_degiskeni = "ftfblog"
if string_degiskeni == "ftfblog.com":
  print("string değişkeni ftfblog.com'a eşittir.")


------------------------------


string_degiskeni = "ftfblog"
if string_degiskeni != "ftfblog.com":
  print("string değişkeni ftfblog.com'a eşit değildir.")


------------------------------


ornek_degisken = "on"
if ornek_degisken == "off":
  print("örnek değişkenimiz ile 'off' eşittir." )
else:
  print("örnek değişkenimiz ile 'off' eşit değildir.")


------------------------------


degisken = "ilkokul"
if degisken == "ortaokul":
  print("değişkenimiz ile 'ortaokul' eşittir." )
elif degisken == "lise":
    print("değişkenimiz ile 'lise' eşittir." )
else:
  print("değişkenimiz ile 'ilkokul' eşittir.")


------------------------------


degisken = "telefon"
if degisken == "tablet":
  print("değişkenimiz ile 'tablet' eşittir." )
elif degisken == "bilgisayar":
    print("değişkenimiz ile 'bilgisayar' eşittir." )
else:
  print("değişkenimiz ile 'telefon' eşittir.")


------------------------------


sayı = 15
if sayı < 20:
  print("15 20'den küçüktür.")


------------------------------


sayı = 20
if sayı > 15:
  print("20 15'den küçüktür.")


------------------------------


sayı = 35
if sayı >= 35:
  print("sayı ya 35'e eşit yada 35'den büyük")
if sayı >= 30:
  print("sayı ya 30'e eşit yada 30'dan büyük")


------------------------------


sayı = 40
if sayı <= 35:
  print("sayı ya 35'e eşit yada 35'ten küçüktür.")
else:
  print("sayı ne 35'e eşit ne de 35'den küçüktür.")


------------------------------


liste_ornek = ["1","2","3","4"]
if "1" in liste_ornek:
  print("1 liste_ornek değişkenin içerisinde mevcuttur.")


------------------------------


sayı = 15
if sayı == 15 and sayı < 20:
    print("Sayı değişkeni 15'e eşit ve 20'den küçüktür.")


------------------------------


sayı = 15
if sayı == 17 or sayı < 20:
  print("Sayı değişkeni 17'e eşit veya 20'den küçüktür.")

------------------------------ FTFBLOG.COM ------------------------------