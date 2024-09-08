import os  
os.system('clear')

file = open("T1.txt", "r", encoding="utf-8")

malumot = file.read()

print(malumot.count("\n"), "ta qatordan iborat")

file.close()