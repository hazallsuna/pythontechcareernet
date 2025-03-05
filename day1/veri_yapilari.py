kitap_turu = ["polisiye","korku","çocuk"] #liste oluşturma
print(kitap_turu)

print(kitap_turu[0])
print(kitap_turu[-1])

#kitap_turu[2] = "roman"
#print(kitap_turu) en son yazılanı çağırır hep

kitap_turu.append("hikaye") #sondan ekliyoruz
kitap_turu.insert(1,"şiir") #1.index yerine ekledik
kitap_turu.remove("çocuk")
print(kitap_turu)

for kitap in kitap_turu:
    print(kitap) #alt alta yazdık

demetler = ("polisiye","korku","çocuk") #tuple tanımlandı

#demetler[1] = "anı" #tuple oluşturduktan sonra değişmez
#demetler.append("gezi")
print(demetler)

calisan = { #sözlük oluşturduk
    "ad": "Ayşe",
    "soyad": "Gündoğar",
    "yas" : 29
}

print(calisan["ad"])

calisan["sehir"] = "İstanbul"
print(calisan)

diller = {"C#","Java","Javascript","Python"} #set üzerinde değişiklik yapılmaz ve aynı eleman eklenmez
#diller.append("C#") yanlış kullanım
print(diller)