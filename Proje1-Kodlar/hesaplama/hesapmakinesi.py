def hmmenü():
     print("╔"+"══════════════════"+"╗")
     print("║ Hesap Makinesi   ║")
     print("║  1- Toplama      ║")
     print("║  2- Çıkarma      ║")
     print("║  3- Çarpma       ║")
     print("║  4- Bölme        ║")
     print("║  Seçimini yap:   ║")
     print("╚"+"══════════════════"+"╝") 
     soru=int(input("Seçimi yap:"))
          
     a= int(input("ilk sayıyı giriniz: "))
     b= int(input("ikinci sayıyı giriniz: ")) 

     def toplama(a,b):
          return a+b

     def çıkarma(a,b):
          return a-b

     def çarpma(a,b):
          return a*b

     def bölme(a,b):
          return a/b

     if soru==1 : 
          print("Sonuç: ", toplama(a,b))
     elif soru==2 :
          print("Sonuç: ", çıkarma(a,b))
     elif soru==3 :
          print("Sonuç: ", çarpma(a,b))
     else :
          print("Sonuç: ", bölme(a,b))
     