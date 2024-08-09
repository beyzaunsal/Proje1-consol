# a =5
# b = "5"
# print(a*2)
# print(type(a))
# print(b*2)
# print(type(b))

# class Ogrenci: # referans, model
#     adi = "Mustafa"
#     soyadi = "ALP"
#     numarasi = "547"
#     def __init__(self,xx,yy):
#         self.adi = xx
#         self.no = yy

# print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi)

# ogrenci1 = Ogrenci()
# print("o1:",ogrenci1.adi)
# ogrenci1.bilgi() 
# ogrenci2 = Ogrenci()
# print("o2:",ogrenci2.adi)

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

class Ogrenci:          #Sınıf isimlerinin baş harfi büyük hafrle yazılır.
    AdSoyad= "tanımsız"
    NotOrtalaması=""
    DisiplinCezası=0
    # aldığıDersler=["ders listesi boş"]

    def __init__(self,ad,no):    #def __init__(self,ad,no=""): yaparsan numara girme zorunluluğunu kaldırır. Ayrıca__init__ olmak zorunda
        self.AdSoyad = ad
        self.Numara= no
        # self.aldığıDersler.append(ad)
        self.aldığıDersler=[]
    
    def bilgi(self):
        print("\n\nmetod ile: Adı Soyadı:",self.AdSoyad,",Numarası:",self.Numara)
        print("Dersler:",*self.aldığıDersler,sep=",") 

    def ders_ekle(self,ww):
        self.aldığıDersler.append(ww)

    def ders_listesi(self):
        print("\n\n dersler listeleniyor")
        print(*self.aldığıDersler,sep="\n")    

print("sınıftaki adsoyad değeri:",Ogrenci.AdSoyad)
ogrenci1=Ogrenci("ahmet bal",10) 
ogrenci2=Ogrenci("veli gül",15)
# ogrenci1.ders_listesi()
ogrenci1.ders_ekle("matematik")
ogrenci1.ders_ekle("türkçe")
ogrenci1.ders_ekle("fizik")
ogrenci1.ders_listesi()
ogrenci1.bilgi()       
ogrenci2.bilgi()