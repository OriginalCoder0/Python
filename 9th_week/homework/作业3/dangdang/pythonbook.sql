# Host: localhost  (Version: 5.5.53)
# Date: 2018-09-25 18:07:46
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;
CREATE DATABASE `dangdang`; /*!40100 DEFAULT CHARACTER SET utf8 */

#USE dangdang;
#
# Structure for table "pythonbook"
#

DROP TABLE IF EXISTS `pythonbook`;
CREATE TABLE `pythonbook` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `pic` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `pubdate` varchar(255) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=559 DEFAULT CHARSET=utf8;

/*!40000 ALTER TABLE `pythonbook` ENABLE KEYS */;