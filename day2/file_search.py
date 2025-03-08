import os

if os.path.exists("day2/example.txt"):
    os.remove("day2/example.txt")
    print("Dosya silindi!")
else:
    print("Dosya bulunamadı!")