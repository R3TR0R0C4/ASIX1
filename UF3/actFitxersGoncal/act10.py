from os import listdir

lsDirectori=listdir("act10")
for fitxer in lsDirectori:
    if ".txt" in fitxer:
        print(fitxer)
