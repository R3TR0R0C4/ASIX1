<?php
//connexi� BD del servidor local
 $conn = mysqli_connect("localhost","root","mysql", "taller_xml"); // Connexi� servidor Mysql
 if (!$conn) {
 	die('Could not connect:' . mysql_error()); // Comprovem la connexi�
 }
//echo 'Connected successfully';
//mysql_select_db("taller_xml"); // Escollim Base de Dades

//connexi� BD per al nostre hosting a 000webhost 
// mysql_connect("mysql1.000webhost.com","taller_xml","*** contrasenya *****"); // Connexi� servidor Mysql
// mysql_select_db("taller_xml"); // Escollim Base de Dades


// Cap�alera fitxer XML a generar

header("Content-type: text/xml");
$t = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>" .chr(13).chr(10) ;
$t .="<rss VERSION=\"2.0\">" . chr(13) . chr(10);

$t .= "<channel>" . chr(13) . chr(10);
//Creem el canal amb la informaci� de l'emisor de noticies
$t .="<title> Noticies Star Wars </title>" . chr(13) . chr(10);
$t .="<link> http://www.starwars.com </link>" .chr(13). chr(10);
$t .="<language> ca </language>" . chr(13) . chr(10) ;
$t .="<webMaster> Maestro Yoda </webMaster>" . chr(13) . chr(10);
$t .="<copyright> CCC </copyright> " . chr(13) . chr(10) ;
$t .="<pubDate>" . date('D, d M Y g:i:s O', time()) . "</pubDate>" . chr(13) . chr(10) ;

$res=mysqli_query($conn,"SELECT * FROM noticies ORDER BY id DESC LIMIT 10"); // consulta Mysql de les 10 ultimes noticies

// A partir de la consulta anirem omplint cada node "item"
for($x=0; $x < mysqli_num_rows($res);$x++) // Bucle per recorrer tots els registres
{
	$t .="<item>" . chr(13) . chr(10) ;
	$t .="<title>" . mysqli_fetch_array($res,$x) . "</title>" . chr(13) . chr(10) ;
	$t .="<guid>" . mysqli_fetch_array($res,$x) . "</guid>" . chr(13) . chr(10) ;
	$t .="<description><![CDATA[" . mysqli_fetch_array($res,$x) . "]]></description>" . chr(13) . chr(10) ;
	$t .="</item>" . chr(13) . chr(10) ;
}

$t .="</channel>" . chr(13) . chr(10) ;
$t .="</rss>" ;

echo $t ;
?>
