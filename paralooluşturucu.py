import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))


parola = ""


for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)


print("Oluşturulan Parola:", parola)



#import string


#kucuk_harfler = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'


#buyuk_harfler = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#tum_harfler = string.ascii_letters      # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


#rakamlar = string.digits                # '0123456789'


#noktalama = string.punctuation          # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 


#bosluk = string.whitespace               # ' \t\n\r\x0b\x0c' #Boşluk karakterleri için kullanılan Kodlar Aklına Yaz !

#yazdirilabilir_karakterler = string.printable

# print("Küçük harfler:", kucuk_harfler)
# print("Büyük harfler:", buyuk_harfler)
# print("Tüm harfler:", tum_harfler)
# print("Rakamlar:", rakamlar)
# print("Noktalama işaretleri:", noktalama)
# print("Boşluk karakteri:", bosluk)
# print("Yazdırılabilir karakterler:", yazdirilabilir_karakterler)
