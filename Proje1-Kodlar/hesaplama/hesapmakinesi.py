print("╔"+"══════════════════"+"╗")
print("║ Hesap Makinesi   ║")
print("║  1- Toplama      ║")
print("║  2- Çıkarma      ║")
print("║  3- Çarpma       ║")
print("║  4- Bölme        ║")
print("║  Seçimini yap:   ║")
print("╚"+"══════════════════"+"╝")
soru=int(input("Seçimi yap:")) 
if soru==1 :
     print("Toplama işlemini seçtiniz.") 
elif soru==2 : 
     print("Çıkarma işlemini seçtiniz.")  
elif soru==3 : 
     print("Çarpma işlemini seçtiniz.")
else:
     print("Bölme işlemini seçtiniz. ")
     
a= int(input("ilk sayıyı giriniz"))
b= int(input("ikinci sayıyı giriniz"))

def toplama(a,b):
     return a+b

def çıkarma(a,b):
     return a-b 

def çarpma(a,b):
     return a*b

def bölme(a,b):
      return a/b


