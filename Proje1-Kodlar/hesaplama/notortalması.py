def ders():    
    b_yazılı=int(input("Birinci yazılı notunuz nedir?"))
    i_yazılı=int(input("İkinci yazılı notunuz nedir?"))
    p_ödev=int(input("Performans ödevi notunuz nedir?"))

    def notlar(b_yazılı,i_yazılı,p_ödev):
        return (b_yazılı+i_yazılı+p_ödev)/3

    ortalama=notlar(b_yazılı,i_yazılı,p_ödev)

    print(f"Not ortalamanız: {ortalama} dir.")
    input()