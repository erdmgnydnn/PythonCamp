#İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

""" n=20
sayi1=1
sayi2=1

print(sayi1, end=" ")

print(sayi2, end=" ")

for i in range(n-2):
    sayi3=sayi1+sayi2
    print(sayi3, end=" ")
    sayi1=sayi2
    sayi2=sayi3  """

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

""" 
sayi = int(input("Bir sayı girin: "))
bolentoplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        bolentoplam += i

if bolentoplam == sayi:
    print(sayi, "mükemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir.")  """


#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

""" sayi1=int(input(("birinci sayıyı giriniz: ")))
sayi2=int(input(("ikinci sayıyı giriniz: ")))

enkucuk=sayi1
if sayi2<enkucuk:
    enkucuk=sayi2

for i in range(1,enkucuk+1):
    if sayi1%i==0 and sayi2%i==0:
        ebob=i

print("Girilen sayıların ebobu: ", i)  """


""" sayi1=int(input(("birinci sayıyı girini: ")))
sayi2=int(input(("ikinci sayıyı girini: ")))

carpim= int(sayi1*sayi2)

for i in range(1,carpim+1):
    if i%sayi1==0 and i%sayi2==0:
        ekok=i
        print("Girilen sayılarun ekoku: ", ekok)
        break
 """

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.


""" sayi=int(input("sayıyı girini: "))

for i in range(2,sayi+1):
    if sayi%i==0:
        if i==sayi:
            print(sayi,"bir asal sayıdır")
            break
        else:
            print(sayi, "bir asal sayı değildir")
            break """


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

""" sayi = int(input("bir sayı gir:"))
print(sayi, "sayısının asal çarpanları:")

bölen=2
for i in range(1,sayi):
    if(sayi%bölen==0):
      print(bölen)
      sayi/=bölen 
    else:
      bölen+=1
 """