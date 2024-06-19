from os import listdir,chdir
from shutil import copy

chdir("act11")

lsDirectori=listdir()
for fitxer in lsDirectori:
    if ".txt" in fitxer:
        copy(fitxer,dst="text_pla")
    