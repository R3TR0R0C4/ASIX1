# Instalació i configuració del servidor FOG

Per instal·lar el servidor entrarém amb usuari root, i utilitzarém git per clonar el repositori de fogproject:

![](imatges/instalServer/fogInstalacio1.png)

<br>

Iniciem l'instalació amb l'script `bin/installfog.sh`. Iniciarém l'instal·lació indicant que utilitzem un servidor basat en debian:

![](imatges/instalServer/fogInstalacio2.png)

<br>

Com aquest serà l'unic servidor que instal·larém el configurem com un servidor `Normal`:

![](imatges/instalServer/fogInstalacio3.png)

<br>

Sel·leccionarém l'interfície `enp0s8` per donar el servei:

![](imatges/instalServer/fogInstalacio4.png)

<br>

Necessitem un servidor DHCP, deixarém que el propi servidor s'encarregui de donar DHCP

![](imatges/instalServer/fogInstalacio5.png)

<br>

Ens demana si volem instal·lar traducció, ssl, si volem cambiar el hostname del servidor i si volem compartir informació amb el FogProject:

![](imatges/instalServer/fogInstalacio6.png)

<br>

Confirmem que l'informació sigui correcta avans de començar l'instal·lació:

![](imatges/instalServer/fogInstalacio7.png)

<br>

Comença l'instal·lació:

![](imatges/instalServer/fogInstalacio8.png)

<br>

Necessitem configurar la base de dades, ho farém entrant a l'ip del servidor, `x.x.x.x/fog/management`:

![](imatges/instalServer/fogInstalacio9.png)

<br>

Com aquesta és una instal·lació des-de net, ens saltarém fer un backup de la BD existent:

![](imatges/instalServer/fogInstalacio10.png)

<br>

I aquesta és l'interfície de Management del servidor una vegada acabada l'instal·lació:

![](imatges/instalServer/fogInstalacio11.png)