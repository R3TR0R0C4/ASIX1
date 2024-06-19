# Instalació i configuració d'un client

## Instal·lació en un client Ubuntu 22.04

Com el servidor fog només té paquets d'instal·lació .exe, primer necessitarém una capa de compatibilitat que es diu [mono](https://www.mono-project.com/):

![](imatges/instalClient/fogClient1.png)

<br>

Després descarregarem el paquet `SmartInstaller.exe` del servidor:

![](imatges/instalClient/fogClient2.png)

<br>

Iniciarém l'instal·lació del client amb `sudo mono SmartInstaller.exe`.

![](imatges/instalClient/fogClient3.png)

<br>

Configurem IP del servidor, l'adreça del webroot, podem habilitar si volem una icona a la tray, i si volem auto-iniciar:

![](imatges/instalClient/fogClient4.png)

<br>

Després farém un cat del .log resultant, i comprobém que s'hagi instal·lat correctament

![](imatges/instalClient/fogClient5.png)



## Instal·lació en un client Windows 10 

Per instal·lar el client de windows no necessitem paquets adicionals, podem descarregar el `Smart Installer` i instal·lar-lo directament.

![](imatges/instalClient/fogClientW1.png)

<br>

En el procés d'instal·lació necessitem indicar l'adreça del servidor, les demés opcións les podem deixar per defecte

![](imatges/instalClient/fogClientW2.png)

<br>

Després necessitem reiniciar la màquina, i iniciar el sistema per xarxa, ens sortirà el menú PXE del fog, necessitem l'opció `Aoorive This Host`:

![](imatges/instalClient/fogClientW3.png)

<br>

Introduïrem les credencials:

![](imatges/instalClient/fogClientW4.png)

<br>

I ens ha de dire que s'ha aprovat correctament:

![](imatges/instalClient/fogClientW5.png)

<br>

Una vegada fet tot aixó podrém tornar a la WebUI i veurém un nou equip registrat:

![](imatges/instalClient/fogClientW6.png)
