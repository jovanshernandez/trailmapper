-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: dreamteam_db
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('0d5b65c290b4');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (3,'Tony Hwang Campaign','Campaign for Tony Hwang'),(4,'Corky Messner Campaign','Campaign for Corky Messner'),(5,'Surus Political Team','Surus Political Team'),(6,'Unassaigned','No campaign assignment'),(7,'Trailmapper Demo ','Trailmapper Demo '),(8,'Trailmapper Sandbox','Use this to test things out!'),(9,'New User 1 Campaign ','New User 1 Campaign '),(10,'New User 2 Campaign ','New User 2 Campaign');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) DEFAULT NULL,
  `username` varchar(60) DEFAULT NULL,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_employees_email` (`email`),
  UNIQUE KEY `ix_employees_username` (`username`),
  KEY `department_id` (`department_id`),
  KEY `role_id` (`role_id`),
  KEY `ix_employees_first_name` (`first_name`),
  KEY `ix_employees_last_name` (`last_name`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'jovan@trailmapper.io','jovan','Jovan','Hernandez','pbkdf2:sha256:150000$6llkw5YW$7d2b07e11d8d639ba7cbf15f6581e95de6e34c7118f3d78ad62b0d09f2aa2436',7,1,0),(2,'admin@trailmapper.io','admin',NULL,NULL,'pbkdf2:sha256:150000$8vFmEoVu$21e033a0c72975efae4a7a1252faab97faa8667364b5580dc665d30981987c97',NULL,NULL,1),(7,'brendan@trailmapper.io','Brendan','Brendan','Manning','pbkdf2:sha256:150000$kRi4iBRY$b2a49a66338db7594bd9fa798c747e7dffbf607c167ddfa57cc4d25418744e1e',4,1,0),(8,'dante@trailmapper.io','Trailmapper','Dante','Vitagliano','pbkdf2:sha256:150000$bMiWbtYU$a5411aff14646dab56ab677c9375729b2499a186bcb8ef294e352f4244e65a53',4,1,0),(9,'test@trailmapper.io','Test User','Test','User','pbkdf2:sha256:150000$AhSBH8vI$4f842f508d8b23ae01a1fa98a742ecb60bba298e8355e6f53220715140f129c7',8,1,0),(12,'philippe@trailmapper.io','philippe','Philippe','Melin','pbkdf2:sha256:150000$zymukicT$5f04fc19fe212e54d8c7c108ec7314890046a02db3505164f132b6ad2f3b928a',5,1,0),(13,'demo@trailmapper.io','Demo User ','Demo','User ','pbkdf2:sha256:150000$yK5nFOEo$98049443297b967427641b112eb41dc56a926f255130222f4f839618935d9ac2',7,1,0),(14,'surus@trailmapper.io','Surus Political ','Surus','Political ','pbkdf2:sha256:150000$IH4g1MoX$0822e683d7aa8daa12612af869544a62e0e254784b0c067db27751528323711a',5,1,0),(15,'sandbox@trailmapper.io','Sandbox','Sand','Box','pbkdf2:sha256:150000$EkcEYlXw$8449576a0c016e1cf65797fae09bdee76a9a9bf171d789a91d70b36c37297dff',8,1,0),(16,'tony@trailmapper.io','Hwang','Tony','Hwang','pbkdf2:sha256:150000$reJ3klAJ$b1b169d38edd45823b6d9f55c64c3fb4e1da8a374562a9713f58d525b15a7fd3',3,1,0),(17,'demo@yourdomain.com','Your Campaign','Your ','Campaign','pbkdf2:sha256:150000$7Nf9N0r4$57f3e40a629da41cd4732faa2885061f2d81c317556f6a8b0d3bbd6b23a0f216',7,1,0),(18,'committee@jsyversen.com','committee@jsyversen.com','Jason ','Syversen','pbkdf2:sha256:150000$gFXWycec$511b51080dc5fa914da59ec7502a06d56788213050c259ada7545c3e7741c080',NULL,NULL,0),(19,'new@new.com','testing-new-user','new','user','pbkdf2:sha256:150000$goNE0O5s$1114d68409a45cd9d833d66267ccedb6dbe804730f0ba6bcaf7356cb54f357ce',9,1,0);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Manager','Manager level role'),(2,'Staffer','Staff level role'),(3,'Volunteer','Volunteer level role');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-07  7:35:34
