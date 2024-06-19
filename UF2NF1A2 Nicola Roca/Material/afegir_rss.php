<?php
//connexió BD del servidor local
 $conn = mysqli_connect("localhost","root","mysql", "taller_xml"); // Connexió servidor Mysql
 if (!$conn) {
 	die('Could not connect:' . mysql_error()); // Comprovem la connexió
 }
//echo 'Connected successfully';
//mysql_select_db("taller_xml"); // Escollim Base de Dades

//connexió BD per al nostre hosting a 000webhost 
// mysql_connect("mysql1.000webhost.com","taller_xml","*** contrasenya *****"); // Connexió servidor Mysql
// mysql_select_db("taller_xml"); // Escollim Base de Dades


$sx = simplexml_load_file('http://blog.stuartherbert.com/php/feed/'); // carrega el fitxer XML de la font RSS que li indiquem 

// llegeix la informació del canal 
foreach($sx->channel as $item)
{

	$tit = addslashes($item->title);
	echo $tit ."<br>";
	echo $item->link ."<br>";
	echo $item->language ."<br>";
	echo $item->copyright;
	echo $sx;
	$cp = addslashes($item->copyright); 
	echo $cp ."<br>";

	// Grava les dades del canal a la taula "canals"

	if (mysqli_query($conn,"INSERT INTO canals (data_alta,title,link,language,copyright) VALUES (NOW(),'$tit','$item->link','$item->language','$cp') ") ) echo "Registre afegit <br/>" . $item->nom;
	else echo "Error en la gravació <br> ";
}
echo "Hem gravat la capçalera <br/>"; 

// recupera la id d'aquest canal en la nostra taula Mysql 
$res = mysqli_query($conn,"SELECT id FROM canals WHERE title = '$tit'"); 
$id = mysqli_fetch_row($res);
//echo $id[0];


// Llegirem noticies 
foreach($sx->channel->item as $item)
{
	$tit = addslashes($item->title);
	echo $tit ."<br>";
	echo $item->link ."<br>";
	echo $item->guid ."<br>";
	// L'addslahes ens afegueix les barres "/" per evitar tenir problemes amb els caràcters especials com les cometes ,,,, 
	$descri = addslashes($item->description);  
	echo $descri . "<br>";

	// Grava cada noticia llegida del RSS a la taula de noticies 
	if (mysqli_query($conn,"INSERT INTO noticies (id_canal,data,title,guid,description) VALUES ($id[0],NOW(),'$tit','$item->guid','$descri') ") ) echo "Registre afegit <br/>" . $tit ;
	else echo "Error en la gravació <br/> ";
}
echo "Fi de la gravació <br/>";
?>
