
import random, turtle 
'''
#renkler =["cyan", "red", "yellow","olive","blue","green"]
turtle.speed(10)
for x in range(20,300,1):
    turtle.color(renkler[x%6])
    turtle.forward(x)
    turtle.right(20)

input()   
'''

#import random
#print(random.random(1,100))

#meyveler=["elma","armut","nar","muz"]
#print(random.choice(meyveler))

for a in range (10):

    turtle.up()
    turtle.goto(random.randint(-200,200),random.randint(-200,200))
    turtle.down()

