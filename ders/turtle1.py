
import random, turtle 
'''
#renkler =["cyan", "red", "yellow","olive","blue","green"]
turtle.speed(10)
for x in range(20,300,1):
    turtle.color(renkler[x%6])
    turtle.forward(x)
    turtle.right(20)

input()   


#import random
#print(random.random(1,100))

#meyveler=["elma","armut","nar","muz"]
#print(random.choice(meyveler))

for a in range (10):

    turtle.up()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.down()


not5=45
print(type(not5))
sehir="ankara"
print(type(sehir))
a=4.5
print(type(a))

tt=aa=vv=8
print(aa*2)

adi, soyadi, numarasi= "beyza", "ünsal", 20370075
print(adi, soyadi, numarasi)

print(f"tt değişkeni{type(tt)}türünde ve değeri {tt}")
print(tt*2)
tt = str(tt)
print(tt*2)

a=5
a=6
def topla():
    a=7
    print("içte:",a)
def carp():
    global a
    a=8
    print("çarpta:",a)

topla()   
print("dışta:",a) 
carp()
'''