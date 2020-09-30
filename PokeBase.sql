-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: POKEBASE
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
-- Table structure for table `ABILITY`

DROP DATABASE IF EXISTS POKEBASE;
CREATE SCHEMA POKEBASE;
USE POKEBASE;

DROP TABLE IF EXISTS `ABILITY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ABILITY` (
  `PokedexID` int(4) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Description` varchar(100) NOT NULL,
  PRIMARY KEY (`PokedexID`),
  CONSTRAINT `ABILITY_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ABILITY`
--

LOCK TABLES `ABILITY` WRITE;
/*!40000 ALTER TABLE `ABILITY` DISABLE KEYS */;
/*!40000 ALTER TABLE `ABILITY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHAMPION`
--

DROP TABLE IF EXISTS `CHAMPION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CHAMPION` (
  `PokedexID` int(4) NOT NULL,
  `Move1` varchar(30) NOT NULL,
  `Move2` varchar(30) NOT NULL,
  `Move3` varchar(30) NOT NULL,
  `Move4` varchar(30) NOT NULL,
  PRIMARY KEY (`PokedexID`),
  KEY `PokedexID` (`PokedexID`,`Move1`),
  KEY `PokedexID_2` (`PokedexID`,`Move2`),
  KEY `PokedexID_3` (`PokedexID`,`Move3`),
  KEY `PokedexID_4` (`PokedexID`,`Move4`),
  CONSTRAINT `CHAMPION_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`),
  CONSTRAINT `CHAMPION_ibfk_2` FOREIGN KEY (`PokedexID`, `Move1`) REFERENCES `POKEMOVES` (`PokedexID`, `Move`),
  CONSTRAINT `CHAMPION_ibfk_3` FOREIGN KEY (`PokedexID`, `Move2`) REFERENCES `POKEMOVES` (`PokedexID`, `Move`),
  CONSTRAINT `CHAMPION_ibfk_4` FOREIGN KEY (`PokedexID`, `Move3`) REFERENCES `POKEMOVES` (`PokedexID`, `Move`),
  CONSTRAINT `CHAMPION_ibfk_5` FOREIGN KEY (`PokedexID`, `Move4`) REFERENCES `POKEMOVES` (`PokedexID`, `Move`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHAMPION`
--

LOCK TABLES `CHAMPION` WRITE;
/*!40000 ALTER TABLE `CHAMPION` DISABLE KEYS */;
/*!40000 ALTER TABLE `CHAMPION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IMMUNITIES`
--

DROP TABLE IF EXISTS `IMMUNITIES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IMMUNITIES` (
  `Name` varchar(20) NOT NULL,
  `Immunity` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`,`Immunity`),
  CONSTRAINT `IMMUNITIES_ibfk_1` FOREIGN KEY (`Name`) REFERENCES `TYPE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IMMUNITIES`
--

LOCK TABLES `IMMUNITIES` WRITE;
/*!40000 ALTER TABLE `IMMUNITIES` DISABLE KEYS */;
/*!40000 ALTER TABLE `IMMUNITIES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LEGENDARY`
--

DROP TABLE IF EXISTS `LEGENDARY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LEGENDARY` (
  `PokedexID` int(4) NOT NULL,
  `Lore` varchar(100) NOT NULL,
  PRIMARY KEY (`PokedexID`),
  CONSTRAINT `LEGENDARY_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LEGENDARY`
--

LOCK TABLES `LEGENDARY` WRITE;
/*!40000 ALTER TABLE `LEGENDARY` DISABLE KEYS */;
/*!40000 ALTER TABLE `LEGENDARY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MOVES`
--

DROP TABLE IF EXISTS `MOVES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MOVES` (
  `Name` varchar(30) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Accuracy` int(3) DEFAULT NULL,
  `Category` varchar(10) NOT NULL,
  `PP` int(2) NOT NULL,
  `Power` int(3) DEFAULT NULL,
  `Type` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`),
  KEY `Type` (`Type`),
  CONSTRAINT `MOVES_ibfk_1` FOREIGN KEY (`Type`) REFERENCES `TYPE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MOVES`
--

LOCK TABLES `MOVES` WRITE;
/*!40000 ALTER TABLE `MOVES` DISABLE KEYS */;
/*!40000 ALTER TABLE `MOVES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POKEMON`
--

DROP TABLE IF EXISTS `POKEMON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `POKEMON` (
  `PokedexID` int(4) NOT NULL,
  `Generation` int(2) NOT NULL,
  `Tier` varchar(4) NOT NULL,
  `EvolvesFrom` int(4) DEFAULT NULL,
  PRIMARY KEY (`PokedexID`),
  KEY `EvolvesFrom` (`EvolvesFrom`),
  CONSTRAINT `POKEMON_ibfk_1` FOREIGN KEY (`EvolvesFrom`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POKEMON`
--

LOCK TABLES `POKEMON` WRITE;
/*!40000 ALTER TABLE `POKEMON` DISABLE KEYS */;
/*!40000 ALTER TABLE `POKEMON` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POKEMOVES`
--

DROP TABLE IF EXISTS `POKEMOVES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `POKEMOVES` (
  `PokedexID` int(4) NOT NULL,
  `Move` varchar(30) NOT NULL,
  PRIMARY KEY (`PokedexID`,`Move`),
  KEY `Move` (`Move`),
  CONSTRAINT `POKEMOVES_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`),
  CONSTRAINT `POKEMOVES_ibfk_2` FOREIGN KEY (`Move`) REFERENCES `MOVES` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POKEMOVES`
--

LOCK TABLES `POKEMOVES` WRITE;
/*!40000 ALTER TABLE `POKEMOVES` DISABLE KEYS */;
/*!40000 ALTER TABLE `POKEMOVES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POKENAME`
--

DROP TABLE IF EXISTS `POKENAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `POKENAME` (
  `PokedexID` int(4) NOT NULL,
  `Name` varchar(30) NOT NULL,
  PRIMARY KEY (`PokedexID`),
  UNIQUE KEY `Name` (`Name`),
  CONSTRAINT `POKENAME_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POKENAME`
--

LOCK TABLES `POKENAME` WRITE;
/*!40000 ALTER TABLE `POKENAME` DISABLE KEYS */;
/*!40000 ALTER TABLE `POKENAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POKETYPE`
--

DROP TABLE IF EXISTS `POKETYPE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `POKETYPE` (
  `PokedexID` int(4) NOT NULL,
  `Type1` varchar(20) NOT NULL,
  `Type2` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PokedexID`),
  KEY `Type1` (`Type1`),
  KEY `Type2` (`Type2`),
  CONSTRAINT `POKETYPE_ibfk_1` FOREIGN KEY (`Type1`) REFERENCES `TYPE` (`Name`),
  CONSTRAINT `POKETYPE_ibfk_2` FOREIGN KEY (`Type2`) REFERENCES `TYPE` (`Name`),
  CONSTRAINT `POKETYPE_ibfk_3` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POKETYPE`
--

LOCK TABLES `POKETYPE` WRITE;
/*!40000 ALTER TABLE `POKETYPE` DISABLE KEYS */;
/*!40000 ALTER TABLE `POKETYPE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESISTANCES`
--

DROP TABLE IF EXISTS `RESISTANCES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RESISTANCES` (
  `Name` varchar(20) NOT NULL,
  `Strength` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`,`Strength`),
  CONSTRAINT `RESISTANCES_ibfk_1` FOREIGN KEY (`Name`) REFERENCES `TYPE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESISTANCES`
--

LOCK TABLES `RESISTANCES` WRITE;
/*!40000 ALTER TABLE `RESISTANCES` DISABLE KEYS */;
/*!40000 ALTER TABLE `RESISTANCES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATS`
--

DROP TABLE IF EXISTS `STATS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STATS` (
  `PokedexID` int(4) NOT NULL,
  `HP` int(3) NOT NULL,
  `Atk` int(3) NOT NULL,
  `Def` int(3) NOT NULL,
  `SpA` int(3) NOT NULL,
  `SpD` int(3) NOT NULL,
  `Spe` int(3) NOT NULL,
  PRIMARY KEY (`PokedexID`),
  CONSTRAINT `STATS_ibfk_1` FOREIGN KEY (`PokedexID`) REFERENCES `POKEMON` (`PokedexID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATS`
--

LOCK TABLES `STATS` WRITE;
/*!40000 ALTER TABLE `STATS` DISABLE KEYS */;
/*!40000 ALTER TABLE `STATS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TYPE`
--

DROP TABLE IF EXISTS `TYPE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TYPE` (
  `Name` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TYPE`
--

LOCK TABLES `TYPE` WRITE;
/*!40000 ALTER TABLE `TYPE` DISABLE KEYS */;
/*!40000 ALTER TABLE `TYPE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WEAKNESSES`
--

DROP TABLE IF EXISTS `WEAKNESSES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WEAKNESSES` (
  `Name` varchar(20) NOT NULL,
  `Weakness` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`,`Weakness`),
  CONSTRAINT `WEAKNESSES_ibfk_1` FOREIGN KEY (`Name`) REFERENCES `TYPE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WEAKNESSES`
--

LOCK TABLES `WEAKNESSES` WRITE;
/*!40000 ALTER TABLE `WEAKNESSES` DISABLE KEYS */;
/*!40000 ALTER TABLE `WEAKNESSES` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-29 21:38:19
