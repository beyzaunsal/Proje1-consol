kilo=int(input("Kilonuzu Giriniz (kg):"))
boy=int(input("Boyunuzu Giriniz (cm):"))
boy = boy/100

def bki(kilo,boy):
    return kilo / boy**2 
bki_value = bki(kilo,boy)
if bki_value<= 20:
    print("İdeal kilonun altındasınız.")
elif 20< bki_value <= 25: 
    print("Kilonuz ideal.")
elif 25< bki_value <= 30: 
    print("İdeal kilonun üstündesiniz.")
else: 
    print("İdeal kilonun çok üstündesiniz.")
