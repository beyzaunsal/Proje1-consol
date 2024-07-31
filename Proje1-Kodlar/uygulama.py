import hesaplama.bilmece
import hesaplama.müziktürleri
import hesaplama.ritmiksayma
import hesaplama.yaş
import hesaplama.faiz
import hesaplama.boykiloendeks
import hesaplama.cisim
import hesaplama.notortalması
import hesaplama.daire
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
    print("║  10- RİTMİK SAYMA                   ║")
    print("║  11- ÇIKIŞ                          ║")
    print("║            Seçimini yap:            ║")
    print("╚"+"═════════════════════════════════════"+"╝")
    soru=int(input("Seçimini yap:"))
    print()
    if soru == 1 : 
        print("Hesap Makinesini seçtiniz.")
        hesaplama.hesapmakinesi.hmmenü()    
    elif soru ==2 : 
        print("Müzik türleri hakkında bilgi edinmek istediniz.")
        hesaplama.müziktürleri.müziktür()

    elif soru ==3 :
        print("Not ortalamasını seçtiniz.") 
        hesaplama.notortalması.ders()
    elif soru ==4 :
        print("Dairenin çap ve alanını seçtiniz.")
        hesaplama.daire.çevrealan()
    elif soru==5 :
        print("Bilmece oyununu seçtiniz.") 
        hesaplama.bilmece.bilmeceoyun()
    elif soru==6 :
        print("Cismin düşme süresini seçtiniz.")
        hesaplama.cisim.cisimyüksekliksüre()
    elif soru==7 :
        print("Boy kilo endeksini seçtiniz.")
        hesaplama.boykiloendeks.endeks()
    elif soru==8 :
        print("Yaş hesabı seçtiniz.")
        hesaplama.yaş.yashesaplama()
    elif soru==9 :
        print("Faiz getirisini seçtiniz.")
        hesaplama.faiz.faizhes()
    elif soru==10 :
        print ("Ritmik saymayı seçtiniz.")
        hesaplama.ritmiksayma.ritmiksay()
    elif soru==11 :
        print("Çıkış yapmak istediniz.")
    else: 
        anamenü()
       
anamenü()


# import hesaplama.anamenü as amenü
#import hesaplama.hesapmakinesi as hm
#print(hm.toplama(a,b))
#print(hm.çıkarma(a,b))
#print(hm.çarpma(a,b))
#print(hm.bölme(a,b))

#import hesaplama.boykiloendeks as bki
#print(bki.bki_value(kilo,boy))

#import hesaplama.faiz as faiz
#print(faiz.Birikimlifaiz(n,faiz,para))

#import hesaplama.yaş as yil
#print(yil.yaş(yıl))   

#import hesaplama.notortalması as nort
#print(nort.notlar(b_yazılı,i_yazılı,p_ödev))

#import hesaplama.daire as aç
#print(aç.alan(r))
#print(aç.cevre(r))

#import hesaplama.cisim as düşme
#print(düşme.süre(t))
#print(düşme.yükseklik(h))

#import hesaplama.müziktürleri as mt
#print(mt.m_tür(soru))

#import hesaplama.bilmece as bmc
#print(bmc.bilmece())

#import hesaplama.ritmiksayma as rsayma
#print(rsayma.ritmiksayma())
    

