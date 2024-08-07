# a =5
# b = "5"
# print(a*2)
# print(type(a))
# print(b*2)
# print(type(b))

class Ogrenci: # referans, model
    adi = "Mustafa"
    soyadi = "ALP"
    numarasi = "547"
    def __init__(self,xx,yy):
        self.adi = xx
        self.no = yy

print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)

ogrenci1 = Ogrenci()
print("o1:",ogrenci1.adi)
ogrenci1.bilgi() 
ogrenci2 = Ogrenci()
print("o2:",ogrenci2.adi)

# class Ogrenci():
#     AdSoyad = "Boş"
#     NotOrtalamasi = ""
#     DisiplinCezasi = 100

#     def __init__(self,ad,no):
#         self.AdSoyad = ad
#         self.Numara = no 
        
#     def bilgi(self):
#         print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

# print("Sınıftaki adSoyad değeri:", Ogrenci.AdSoyad)
# ogrenci1 = Ogrenci()
# ogrenci1.bilgi() 
# ogrenci2 = Ogrenci()
# ogrenci2.bilgi()