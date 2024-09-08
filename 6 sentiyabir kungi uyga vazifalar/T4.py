import os
os.system("clear")

fileR = open("T1.txt", "r")
malumotlar = fileR.read()
fileR.close()

fileW = open("odamlar.txt", "w")
fileW.write(malumotlar)

fileW.close()

