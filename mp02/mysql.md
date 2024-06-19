## BDs

-Crear base de dades:

`CREATE DATABASE nom;`

-Eliminar base de dades:

`DROP DATABASE nom;`

-Mostrar bases de dades:

`SHOW databases;`

-Mostrar els camps d'una taula:

`DESCRIBE nomTaula;`

## Taules

-Crear taula:

`CREATE TABLE nom;`

-Mostrar taules (dintre d'una BBDD):

`SHOW tables;`

-Mostra contingut d'una taula:

`SELECT * FROM nom_taula;`

-Mostra contingut d’una taula amb limit:

`SELECT * FROM nom_taula LIMIT nº;`

## Users

-Crear usuari:

`CREATE USER 'username'@'host' IDENTIFIED BY 'password';`

-Mostra els usuaris:

`SELECT User, Host FROM mysql.user;`

-Eliminar usuari:

`DROP USER ‘user’@’host’;`

-Mostrar permissos d’usuari:
`SHOW GRANTS FOR 'user'@'host';`

## Permisos

-Donar permisos a un usuari sobre una taula d'una BD:

`GRANT permís ON nomBD.nomTaula TO 'usuari'@host’;`

-Donar permisos a un usuari sobre unes columnes d’una taula d’una BD:

`GRANT permís (columna1, columna2) ON nomBD.nomTaula TO ‘usuari’@host’;`

-Treure permisos a un usuari sobre una taula d’una BD

`REVOKE permís ON nomBD.nomTaula FROM 'usuari'@host’;`

-Assumint que estem loguejats en un usuari mostrem els permissos:

`SHOW GRANTS;`

-Mostrar els permisos d’un usuari:

`SHOW GRANTS FOR ‘user’@’host’;`

## Rols

-Crear un rol:

`CREATE ROLE nom;`

-Eliminar un rol:

`DROP ROLE nom;`

-Mostrar rols existents:

`SELECT user AS role_name
FROM mysql.user
WHERE host = '%'
AND NOT LENGTH(authentication_string);`

-Donar permís al rol sobre una bd:

`GRANT permis ON nomBD.* TO nomRol;`

-Mostrar permisos del rol:

`SHOW GRANTS FOR nomRol;`

-Activa el rol per un usuari:

`SET ROLE nomRol`

-Assumint que estem loguejats com usuari mostrem els rols actius:

`SELECT CURRENT_ROLE();`

## Altra informació
-Mostrar les columnes d'una taula d'una BD:

`SHOW COLUMNS FROM nomBD.nomTaula`

-Mostrem les files que existeixen en les taules d'una BD

`SELECT table_name, table_rows
FROM information_schema.tables
WHERE table_schema = 'nomBD';`
