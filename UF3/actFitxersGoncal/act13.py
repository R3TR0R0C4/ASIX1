from os import listdir,chdir,mkdir
from shutil import move
chdir("act13")
try:
    chdir("text_pla")
    chdir("../")

except:
    print("error")
    mkdir("text_pla")
    


lsDirectori=listdir()
for fitxer in lsDirectori:
    if ".txt" in fitxer:
        move(fitxer,dst="text_pla")
