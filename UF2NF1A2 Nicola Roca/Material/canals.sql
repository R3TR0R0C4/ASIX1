-- phpMyAdmin SQL Dump
-- version 3.3.0
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 03, 2013 at 11:46 PM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `taller_xml`
--

-- --------------------------------------------------------

--
-- Table structure for table `canals`
--

CREATE TABLE IF NOT EXISTS `canals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_alta` datetime NOT NULL,
  `title` varchar(50) NOT NULL,
  `generator` varchar(50) NOT NULL,
  `link` varchar(200) NOT NULL,
  `language` varchar(5) NOT NULL,
  `webmaster` varchar(50) NOT NULL,
  `copyright` varchar(50) NOT NULL,
  `pubDate` datetime NOT NULL,
  `lastbuildate` datetime NOT NULL,
  `ttl` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `canals`
--

