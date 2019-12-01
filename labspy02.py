print ("Program Mencari Bilangan Terbesar")

bil1 = int(input("Masukan Bilangan 1 = "))
bil2 = int(input("Masukan Bilangan 2 = "))
bil3 = int(input("Masukan Bilangan 3 = "))

if (bil1>bil2) and (bil1>bil3) :
    print()
    print("Bilangan Terbesarnya adalah = ", bil1)
elif(bil2>bil1) and (bil2>bil3) :
    print()
    print("Bilangan Terbesarnya adalah = ", bil2)
else :
    print()
    print("Bilangan Terbesarnya yaitu = ", bil3)

