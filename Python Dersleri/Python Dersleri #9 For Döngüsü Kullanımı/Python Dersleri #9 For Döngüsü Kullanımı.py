liste = ["1","2","3","4","5","6"]
for elemanlar in liste:
      print(elemanlar)

---------------------------------------------

liste = [1,2.34 ,16.7, 123,19]
for elemanlar in liste:
    print(elemanlar)

---------------------------------------------

liste = ["Karpuz" , "Kavun" , "Elma", "Armut" , "Kiraz"]
for meyveler in liste:
    if "erik" == meyveler:
        print("Erik bulundu.")
    else:
        print("Erik bulunamadı.")

---------------------------------------------

tupleverisi = ("python","derslerini","ftfblog’dan", "öğrenin." )
for elemanlar in tupleverisi:
    print(elemanlar)

---------------------------------------------

isimler = [[“Ahmet”,”Mehmet”,”Ali”],[“Ayşe”,”Fatma”,”Hatice”]]
for isim in isimler:
    print(elemanlar)

---------------------------------------------

isimler = [[“Ahmet”,”Mehmet”,”Ali”],[“Ayşe”,”Fatma”,”Hatice”]]
for isim in isimler:
    for isim2 in isim:
       print(isim2)

---------------------------------------------

isimler = [[“Ahmet”,”Mehmet”,”Ali”],[“Ayşe”,”Fatma”,”Hatice”]]
for a,b,c in isimler:
       print(a,b,c)

---------------------------------------------

import time
start_time = time.time()
isimler = [["Ahmet","Mehmet","Ali"],["Ayşe","Fatma","Hatice"]]
for isim in isimler:
  for isim2 in isim:
    print(isim2)
elapsed_time = time.time() - start_time
print(elapsed_time)

---------------------------------------------

import time
start_time = time.time()
isimler = [["Ahmet","Mehmet","Ali"],["Ayşe","Fatma","Hatice"]]
for a,b,c in isimler:
    print(a,b,c)
elapsed_time = time.time() - start_time
print(elapsed_time)

---------------------------------------------

isimler = [["Ahmet","Mehmet","Ali"],["Ayşe","Fatma","Hatice"]]
for a,b,c in isimler:
    print(a,b,c)

---------------------------------------------

dict_degişkeni = {
    "Erkek":"Ahmet",
     "kızlar":"Ayşe"
}
for a in dict_degişkeni.keys():
  print(a)

---------------------------------------------

toplam = 0
for a in range(10):
    toplam += a
print(toplam)