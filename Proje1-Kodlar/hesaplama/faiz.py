def faizhes():    
    n=int(input("Ödeme yapılacak süre nedir?"))
    faiz=int(input("Faiz oranı nedir?"))
    para=int(input("Dönem sonu yatırılan para nedir?")) / 100

    def bfaiz(n, faiz, para):
        return para*(1+faiz**n)

    Birikimlifaiz=bfaiz(n,faiz,para)

    print(f"Dönem sonunda hesaplanan faiz getirisi {Birikimlifaiz}tl'dir.")
    input()

