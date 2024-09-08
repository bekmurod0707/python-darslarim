import os       
os.system("clear")

file = open("T1.txt", "r", encoding="utf-8")

malumot = file.read()

malumot1 = malumot.split()

eng_uzuni = max(malumot1, key=len)

print(eng_uzuni)

file.close()