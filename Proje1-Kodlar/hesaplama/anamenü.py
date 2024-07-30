def anamenü():
    print("╔"+"═════════════════════════════════════"+"╗")
    print("║ VEKTOREL 1. PROJE ANA MENÜ          ║")
    print("║  1- HESAP MAKİNESİ                  ║")
    print("║  2- MÜZİK TÜRLERİ HAKKINDA BİLGİ    ║")
    print("║  3- NOT ORTALAMASI                  ║")
    print("║  4- DAİRENİN ÇAP ve ALAN HESABI     ║")
    print("║  5- BİLMECE OYUNU                   ║")
    print("║  6- CİSMİN DÜŞME SÜRESİ             ║")
    print("║  7- BOY KİLO ENDEKSİ                ║")
    print("║  8- YAŞ HESABI                      ║")
    print("║  9- FAİZ GETİRİSİ                   ║")
    print("║  10- RİTMİK SAYMA                   ║")
    print("║  11- ÇIKIŞ                          ║")
    print("║            Seçimini yap:            ║")
    print("╚"+"═════════════════════════════════════"+"╝")
    soru=input("Seçimini yap:")
    if soru == 1 : 
        print("Hesap Makinesini seçtiniz.")
    elif soru ==2 : 
        print("Müzik Türşeri Hakkında Bilgi Edinmek İstediniz.")
    elif soru ==3 :
        print("Not ortalamasını seçtiniz.") 
    elif soru ==4 :
        print("Dairenin çap ve alanını seçtiniz.")
    elif soru==5 :
        print("Bilmece oyununu seçtiniz.")
    elif soru==6 :
        print("Cismin düşme süresini seçtiniz.")
    elif soru==7 :
        print("Boy kilo endeksini seçtiniz.")
    elif soru==8 :
        print("Yaş hesabını seçtiniz.")
    elif soru==9 :
        print("Faiz getirisini seçtiniz.")
    elif soru==10 :
        print ("Ritmik saymayı seçtiniz.")
    elif soru==11 :
        print("Çıkış yapmak istediniz.")
    else: anamenü()
       
