#dosya okuma
with open("day2/example.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)

#dosyaya yeni bir şey yazıp var olanı değiştirme
with open("day2/example.txt","w",encoding="utf-8") as file:
    file.write("Bu yeni metin.\n")
    
#dosyaya yeni bir şey ekleme
with open("day2/example.txt","a",encoding="utf-8") as file:
    file.write("Bu eklenen satır. \n")

