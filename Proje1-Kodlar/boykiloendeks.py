kilo=float(input("Kilonuzu Giriniz (kg):"))
boy=float(input("Boyunuzu Giriniz (cm):"))
boy/100
bki= kilo / boy**2
if bki<= 20: print("İdeal kilonun altındasınız.")
elif 20< bki <= 25: print("Kilonuz ideal.")
elif 25< bki <= 30: print("İdeal kilonun üstündesiniz.")
else: print("İdeal kilonun çok üstündesiniz.")
input()