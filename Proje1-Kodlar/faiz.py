n=int(input("Ödeme yapılacak süre nedir?"))
faiz=int(input("Faiz oranı nedir?"))
para=int(input("Dönem sonu yatırılan para nedir?")) / 100
Birikimlifaiz=para*(1+faiz**n)
print(f"Dönem sonunda hesaplanan faiz getirisi {Birikimlifaiz}tl'dir.")
input()
