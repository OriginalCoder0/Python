-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `abstract` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `uid` int(10) unsigned DEFAULT NULL,
  `pcount` int(10) unsigned DEFAULT '0',
  `flag` tinyint(3) unsigned DEFAULT '0',
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201807018 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (201807001,'A','AA','aa...aa',1001,10,1,'2018-07-04 11:56:17'),(201807002,'B','BB','bb...bb',1001,8,1,'2018-07-04 11:57:28'),(201807003,'C','CC','cc...cc',1002,5,1,'2018-07-04 11:58:01'),(201807004,'D','DD','dd...dd',1004,12,1,'2018-07-04 11:58:21'),(201807005,'E','EE','ee...ee',1005,7,1,'2018-07-04 11:58:39'),(201807006,'F','FF','ff...ff',1005,10,1,'2018-07-04 11:58:51'),(201807007,'G','GG','gg...gg',1008,2,1,'2018-07-04 11:59:16'),(201807008,'H','HH','hh...hh',1008,0,0,'2018-07-04 11:59:35'),(201807009,'I','II','ii...ii',1007,3,1,'2018-07-04 12:00:06'),(201807010,'J','JJ','jj...jj',1005,6,1,'2018-07-04 12:00:23'),(201807011,'K','KK','kk...kk',1009,1,1,'2018-07-04 12:00:46'),(201807012,'L','LL','ll...ll',1014,8,1,'2018-07-04 12:00:59'),(201807013,'M','MM','mm...mm',1012,0,0,'2018-07-04 12:01:17'),(201807014,'N','NN','nn...nn',1002,4,1,'2018-07-04 12:01:37'),(201807015,'O','OO','oo...oo',1003,1,1,'2018-07-04 12:02:00'),(201807016,'P','PP','pp...pp',1008,0,0,'2018-07-04 12:02:19'),(201807017,'Q','QQ','qq...qq',1001,0,2,'2018-07-04 12:02:44');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1015 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1001,'Allen','allen@csdn.net','2018-07-04 00:07:13'),(1002,'Bob','bob@csdn.net','2018-07-03 00:00:00'),(1003,'Carrie','carrie@csdn.net','2018-07-03 17:53:54'),(1004,'David','david@csdn.net','2018-07-03 23:41:56'),(1005,'Elsa','elsa@csdn.net','2018-07-04 00:03:16'),(1006,'Fifi','fifi@csdn.net','2018-07-04 00:03:35'),(1007,'Gucci','gucci@csdn.net','2018-07-04 00:05:01'),(1008,'Herry','herry@csdn.net','2018-07-04 01:00:23'),(1009,'Irving','irving@csdn.net','2018-07-04 01:00:59'),(1010,'James','james@csdn.net','2018-07-04 01:01:30'),(1011,'Ken','ken@csdn.net','2018-07-04 01:01:46'),(1012,'Lucky','lucky@csdn.net','2018-07-04 01:02:16'),(1013,'Miruna','miruna@csdn.net','2018-07-04 01:02:36'),(1014,'Nike','nike@csdn.net','2018-07-04 01:03:22');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-04 12:48:44
