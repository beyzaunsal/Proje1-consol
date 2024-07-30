n=int(input("Bir sayı giriniz: "))
formül = 0

for i in range(1, n + 1):
  formül += 1 / i

print(f"Toplam: {formül:.2f}")