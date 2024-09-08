import os
os.system("clear")

file = open("T1.txt", "r", encoding="utf-8")

malumot = file.read()

soz = malumot.split("\n")
qator = soz[-1]

print(qator)

file.close()
