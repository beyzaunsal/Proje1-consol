def oyunlar():
    print("╔"+"══════════════════════"+"╗")
    print("║       OYUNLAR        ║")
    print("║  1- Yılan Oyunu      ║")
    print("║  2- Adam Asmaca      ║")
    print("║  3- Taş Kağıt Makas  ║")
    print("║  Seçimini yap:       ║")
    print("╚"+"══════════════════════"+"╝")

    soru = int(input("Seçimini yap: "))

    def yilanoyunu():  
    
     import random
    import turtle
    import time
    delay = 0.15
    
    pencere = turtle.Screen()
    pencere.title('Yılan Oyunu')
    pencere.bgcolor('lightgreen')
    pencere.setup(width=600, height=600)
    pencere.tracer(0)
    
    kafa = turtle.Turtle()
    kafa.speed(0)
    kafa.shape("square")
    kafa.color("black")
    kafa.penup()
    kafa.goto(0, 100)
    kafa.direction = "stop"
    
    yemek = turtle.Turtle()
    yemek.speed(0)
    yemek.shape("circle")
    yemek.color("red")
    yemek.penup()
    yemek.shapesize(0.80, 0.80)
    yemek.goto(0, 0)
    
    kuyruklar = []
    puan = 0
    
    yaz = turtle.Turtle()
    yaz.speed(0)
    yaz.shape("square")
    yaz.color("white")
    yaz.penup()
    yaz.hideturtle()
    yaz.goto(0, 260)
    yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
    
    def move():
        if kafa.direction == "up":
            y = kafa.ycor()
            kafa.sety(y + 20)
        if kafa.direction == "down":
            y = kafa.ycor()
            kafa.sety(y - 20)
        if kafa.direction == "right":
            x = kafa.xcor()
            kafa.setx(x + 20)
        if kafa.direction == "left":
            x = kafa.xcor()
            kafa.setx(x - 20)
    
    def go_up():
        if kafa.direction != "down":
            kafa.direction = "up"
    def go_down():
        if kafa.direction != "up":
            kafa.direction = "down"
    
    
    
    
    
    def go_right():
        if kafa.direction != "left":
            kafa.direction = "right"
    def go_left():
        if kafa.direction != "right":
            kafa.direction = "left"
    
    pencere.listen()
    pencere.onkey(go_up, "Up")
    pencere.onkey(go_down, "Down")
    pencere.onkey(go_right, "Right")
    pencere.onkey(go_left, "Left")
    
    while True:
        pencere.update()
    
        if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
    
            for kuyruk in kuyruklar:
                kuyruk.goto(1000, 1000)
            kuyruklar = []
    
            puan = 0
            delay = 0.1
    
            yaz.clear()
            yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
    
        if kafa.distance(yemek) < 20:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            yemek.goto(x, y)
    
            yeni_kuyruk = turtle.Turtle()
            yeni_kuyruk.speed(0)
            yeni_kuyruk.shape("square")
            yeni_kuyruk.color("white")
            yeni_kuyruk.penup()
            kuyruklar.append(yeni_kuyruk)
    
            delay -= 0.001
    
            puan = puan + 10
            yaz.clear()
            yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
    
        for index in range(len(kuyruklar) - 1, 0, -1):
            x = kuyruklar[index - 1].xcor()
            y = kuyruklar[index - 1].ycor()
            kuyruklar[index].goto(x, y)
    
        if len(kuyruklar) > 0:
            x = kafa.xcor()
            y = kafa.ycor()
            kuyruklar[0].goto(x, y)
    
        move()
    
        for segment in kuyruklar:
            if segment.distance(kafa) < 20:
                time.sleep(1)
                kafa.goto(0, 0)
                kafa.direction = "stop"
                for segment in kuyruklar:
                    segment.goto(1000, 1000)
                kuyruklar = []
                puan = 0
                yaz.clear()
                yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
                hiz = 0.15
    
    
    
    
    
        time.sleep(delay)

    import json
    import os

def adamas():

        try:
            from termcolor import cprint
        except ImportError:
            def cprint(*args, **kwargs):
                print(*args)
        
        kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]
        
        
        def oyun_hazirlik():
            """Oyun için gerekli değişkenleri tanımlar"""
            global secilen_kelime, gorunen_kelime, can
            import random
            secilen_kelime = random.choice(kelimeler)
            gorunen_kelime = ["-"] * len(secilen_kelime)
            can = 5
        
        
        def harf_al():
            """Kullanıcıdan bir harf alır, alana kadar gerekirse hata verir, birisi quit yazarsa programı kapatır"""
            devam = True
            while devam:
                harf = input("Bir harf giriniz: ")
                if harf.lower() == "quit":
                    cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                    exit()
                elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
                    devam = False
                else:
                    cprint("Hatalı Giriş", color="red", on_color="on_grey")
        
            # noinspection PyUnboundLocalVariable
            return harf.lower()
        
        
        def oyun_dongusu():
            """Oyunun ana döngüsü, harf alır, tutarsa görünen karakterler listesi güncellenir,
            tutmazsa can azaltılır, ve bu can bitene kadar ya da kelime bilinene kadar devam eder..."""
            global gorunen_kelime, can
            while can > 0 and secilen_kelime != "".join(gorunen_kelime):
                cprint("kelime: " + "".join(gorunen_kelime), color="cyan", attrs=["bold"])
                cprint("can   : <" + "❤" * can + " " * (5 - can) + ">", color="cyan", attrs=["bold"])
        
                girilen_harf = harf_al()
                pozisyonlar = harf_kontrol(girilen_harf)
                if pozisyonlar:
                    for p in pozisyonlar:
                        gorunen_kelime[p] = girilen_harf
                else:
                    can -= 1
        
        
        def harf_kontrol(girilen_harf):
            """Gelen harfin seçilen kelimede nerelerde olduğunu bulur"""
            poz = []
            for index, h in enumerate(secilen_kelime):
                if h == girilen_harf:
                    poz.append(index)
            return poz
        
        
        def skor_tablosunu_goster():
            """Skor tablosunu gösterir"""
            veri = ayar_oku()
            cprint("|Skor\t\tKullanıcı|", color="white", on_color="on_grey")
            cprint("|------------------------|", color="white", on_color="on_grey")
            for skor, kullanici in veri["skorlar"]:
                cprint("|"+str(skor) +"\t\t"+ kullanici+" "*(9-len(kullanici))+"|", color="white", on_color="on_grey")
            cprint("|------------------------|", color="white", on_color="on_grey")
        
        
        def skor_tablosunu_guncelle():
            """Skor tablosunu son kullanıcının ismiyle ve skoruyla günceller"""
            veri = ayar_oku()
            veri["skorlar"].append((can, veri["son_kullanan"]))
            veri["skorlar"].sort(key=lambda skor_tuplei: skor_tuplei[0], reverse=True)
            veri["skorlar"] = veri["skorlar"][:5]
            ayar_yaz(veri)
        
        
        def oyun_sonucu():
            """Oyun bittiğinde kazanıp kazanamadığımızı ekrana yazar."""
            if can > 0:
                cprint("Kazandınız", color="yellow", on_color="on_red")
                skor_tablosunu_guncelle()
            else:
                cprint("Kaybettiniz", color="red", on_color="on_yellow")
            skor_tablosunu_goster()
        
        
        def dosyay_kontrol_et_yoksa_olustur():
            """Ayar dosyası var mı kontrol eder, varsa sağlam mı diye bakar,
            bozuk ya da olmayan durum için dosyayı öntanımlı değerlerle oluşturur"""
            yaz = False
            if os.path.exists("ayarlar.json"):
                try:
                    ayar_oku()
                except ValueError as e:
                    cprint("Hata: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
                    os.remove("ayarlar.json")
                    yaz = True
            else:
                yaz = True
        
            if yaz:
                ayar_yaz({"skorlar": [], "son_kullanan": ""})
        
        
        def ayar_oku():
            """Ayarlar dosyasını okur"""
            with open("ayarlar.json") as f:
                return json.load(f)
        
        
        def ayar_yaz(veri):
            """Ayarlar dosyasına gönderilen veriyi yazar"""
            with open("ayarlar.json", "w") as f:
                json.dump(veri, f)
        
        
        def kullanici_adini_guncelle():
            """Kullanıcıdan isim alıp ayarlara yazdırmaya gönderir"""
            veri = ayar_oku()
            veri["son_kullanan"] = input("Kullanıcı Adınız: ")
            while not veri["son_kullanan"] or len(veri["son_kullanan"]) > 9:
                veri["son_kullanan"] = input("lykpython ile 9 karakter uzunluğunda yazın: ")
            ayar_yaz(veri)
        
        
        def kullanici_kontrol():
            """Bir önce giriş yapan kullanıcı ismini gösterip kullanıcıya bu siz misiniz diye sorar"""
            veri = ayar_oku()
            print("Son giriş yapan: " + veri["son_kullanan"])
            if not veri["son_kullanan"]:
                kullanici_adini_guncelle()
            elif input("Bu siz misiniz?(e/h) ").lower() == "h":
                kullanici_adini_guncelle()
        
        
        def main():
            """Programın ana döngüsü, oyunun çalışmasından yükümlü"""
            tekrar_edecek_mi = True
            dosyay_kontrol_et_yoksa_olustur()
            cprint("Merhaba, Adam Asmacaya hoşgeldiniz.", color="cyan", on_color="on_magenta", attrs=["bold"])
            cprint("Yardım: Oyun sırasında quit diyerek çıkabilirsiniz", color="cyan", on_color="on_magenta", attrs=["bold"])
            cprint("-"*30, color="cyan", on_color="on_magenta", attrs=["bold"])
            skor_tablosunu_goster()
            kullanici_kontrol()
            while tekrar_edecek_mi:
                oyun_hazirlik()
                oyun_dongusu()
                oyun_sonucu()
                if input("Devam?(e/h) ").lower() == "h":
                    tekrar_edecek_mi = False
        
        main()
        
import random
def play_game():
        choices = ['taş', 'kağıt', 'makas']
        user_score = 0
        computer_score = 0
        
        while True:
            # Kullanıcının seçimini al
            user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ").lower()
            
            if user_choice == 'q':
                print("Oyun sonlandırıldı.")
                break
            
            if user_choice not in choices:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                continue
            
            # Bilgisayarın seçimini belirle
            computer_choice = random.choice(choices)
            
            print(f"Senin seçimin: {user_choice}")
            print(f"Bilgisayarın seçimi: {computer_choice}")
            
            # Oyun sonucunu kontrol et
            if user_choice == computer_choice:
                print("Berabere! Tekrar deneyin.")
            elif (
                (user_choice == 'taş' and computer_choice == 'makas') or
                (user_choice == 'kağıt' and computer_choice == 'taş') or
                (user_choice == 'makas' and computer_choice == 'kağıt')
            ):
                print("Tebrikler! Kazandınız.")
                user_score += 1
            else:
                print("Üzgünüm! Kaybettiniz.")
                computer_score += 1
            
            print(f"Puan Durumu: Sen {user_score} - {computer_score} Bilgisayar")
            
            # Oyunu kontrol et
            if user_score == 10:
                print("Oyun bitti. Tebrikler, Siz kazandınız!")
                break
            elif computer_score == 10:
                print("Oyun bitti. Üzgünüm, Bilgisayar kazandı.")
                break

    # Oyunu oynat
play_game()

if soru==1 : 
    print(yilanoyunu())
elif soru==2 :
    print(adamas())
else:
    print(play_game())
  