from subprocess import run #Importarem el procés "run" del mòdul "subprocess"
comanda=run(["ls -la"], shell=True, capture_output=True, text=True) # farà un ls -la i guardarà el resultat a la variable comanda
#Per llegir el resultat necessitem fer servir arguments:

#Per llegir el resultat de la shell:
print(comanda.stdout)

#Per llegir el resultat de l'error que pot donar:
print(comanda.stderr)

