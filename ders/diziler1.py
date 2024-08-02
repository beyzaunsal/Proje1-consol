import random
tutulan= random.randint(a=1, b=100)
#print(tutulan)
hak=10 
puan=100
for i in range(hak):
    tahmin=int(input("Tahminin ne: "))
    if tahmin==tutulan :
        print("bildin")
        break
    elif tahmin >tutulan:
        puan -=10
        print()
        print()
    elif tahmin < tutulan:
        puan-=10
        print("sayın küçük")
        print("puanın: ",puan )
else:
    print("hakkın bitti")            