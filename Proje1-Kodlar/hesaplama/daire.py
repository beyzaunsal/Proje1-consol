def çevrealan():    
    pi=3.1416
    soru=input("Alan mı hesaplamak istersiniz, Çevre mi?")
    cap=int(input("Dairenin çapı nedir?"))
    r= cap / 2

    def alan(r):
        return pi*r**2

    def cevre(r):
        return 2*pi**r

    if soru.lower() == "alan" :
        print(f"Dairenin alanı : {alan(r):.2f}")
    else:
        print(f"Dairenin çevresi : {cevre(r):.2f}")
            
  

