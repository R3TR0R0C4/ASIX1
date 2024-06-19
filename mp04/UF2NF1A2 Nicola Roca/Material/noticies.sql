-- phpMyAdmin SQL Dump
-- version 3.3.0
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 03, 2013 at 11:58 PM
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
-- Table structure for table `noticies`
--

CREATE TABLE IF NOT EXISTS `noticies` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `id_canal` int(3) NOT NULL,
  `data` datetime NOT NULL,
  `title` varchar(200) NOT NULL,
  `guid` varchar(200) NOT NULL,
  `category` varchar(50) NOT NULL,
  `pubdate` datetime NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

--
-- Dumping data for table `noticies`
--

