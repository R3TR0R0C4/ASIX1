from os import listdir,chdir
from shutil import move

chdir("act12")

lsDirectori=listdir()
for fitxer in lsDirectori:
    if ".txt" in fitxer:
        move(fitxer,dst="text_pla")
    