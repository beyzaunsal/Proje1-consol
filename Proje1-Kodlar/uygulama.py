import hesaplama.bilmece
import hesaplama.müziktürleri
import hesaplama.yaş
import hesaplama.faiz
import hesaplama.boykiloendeks
import hesaplama.cisim
import hesaplama.notortalması
import hesaplama.daire
import hesaplama.oyun
import hesaplama.hesapmakinesi
import hesaplama.notortalması
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
    print("║  10- OYUNLAR                        ║")
    print("║  11- ÇIKIŞ                          ║")
    print("║            Seçimini yap:            ║")
    print("╚"+"═════════════════════════════════════"+"╝")
    soru=int(input("Seçimini yap:"))
    print()
    if soru == 1 : 
        print("Hesap Makinesini seçtiniz.")
        hesaplama.hesapmakinesi.hmmenü()
        anamenü()   
    elif soru ==2 : 
        print("Müzik türleri hakkında bilgi edinmek istediniz.")
        hesaplama.müziktürleri.müziktür()
        anamenü()
    elif soru ==3 :
        print("Not ortalamasını seçtiniz.") 
        hesaplama.notortalması.ders()
        anamenü()
    elif soru ==4 :
        print("Dairenin çap ve alanını seçtiniz.")
        hesaplama.daire.çevrealan()
        anamenü()
    elif soru==5 :
        print("Bilmece oyununu seçtiniz.") 
        hesaplama.bilmece.bilmeceoyun()
        anamenü()
    elif soru==6 :
        print("Cismin düşme süresini seçtiniz.")
        hesaplama.cisim.cisimyüksekliksüre()
        anamenü()
    elif soru==7 :
        print("Boy kilo endeksini seçtiniz.")
        hesaplama.boykiloendeks.endeks()
        anamenü()
    elif soru==8 :
        print("Yaş hesabı seçtiniz.")
        hesaplama.yaş.yashesaplama()
        anamenü()
    elif soru==9 :
        print("Faiz getirisini seçtiniz.")
        hesaplama.faiz.faizhes()
        anamenü()
    elif soru==10 :
        print ("İyi eğlenceler :") 
        hesaplama.oyun.oyunmenü()
        anamenü()
    elif soru==11 :
        print("Çıkış yaptınız.")
    else: 
        anamenü()



anamenü()
