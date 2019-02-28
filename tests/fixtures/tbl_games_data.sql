/*
SQLyog Community v13.1.1 (64 bit)
MySQL - 10.3.9-MariaDB : Database - mais
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mais` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mais`;

/*Table structure for table `tbl_games` */

DROP TABLE IF EXISTS `tbl_games`;

CREATE TABLE `tbl_games` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MatchTime` datetime DEFAULT NULL,
  `MatchTypeID` int(10) unsigned NOT NULL DEFAULT 0,
  `HteamID` int(11) DEFAULT NULL,
  `Hscore` int(11) DEFAULT 0,
  `AteamID` int(11) DEFAULT NULL,
  `Ascore` int(11) DEFAULT 0,
  `VenueID` int(11) DEFAULT NULL,
  `Duration` int(11) unsigned NOT NULL DEFAULT 0,
  `Attendance` int(11) DEFAULT NULL,
  `MeanTemperature` int(3) unsigned DEFAULT NULL COMMENT 'Mean Daily Temperature, from Weather Underground',
  `Precipitation` double(2,1) DEFAULT NULL,
  `WeatherEvents` varchar(255) NOT NULL DEFAULT '""',
  `Notes` text DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `EventDate` (`MatchTime`),
  KEY `HTeamID` (`HteamID`),
  KEY `ATeamID` (`AteamID`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

/*Data for the table `tbl_games` */

insert  into `tbl_games`(`ID`,`MatchTime`,`MatchTypeID`,`HteamID`,`Hscore`,`AteamID`,`Ascore`,`VenueID`,`Duration`,`Attendance`,`MeanTemperature`,`Precipitation`,`WeatherEvents`,`Notes`) values 
(1,'1996-04-06 00:00:00',1,9,1,3,0,9,90,0,NULL,NULL,'\"\"','Sample'),
(2,'1996-04-13 00:00:00',1,2,4,3,0,2,90,0,NULL,NULL,'\"\"','Sample'),
(3,'1996-04-13 00:00:00',1,5,3,1,0,5,90,0,NULL,NULL,'\"\"',NULL),
(6,'1996-04-14 00:00:00',1,3,1,9,0,3,90,0,NULL,NULL,'\"\"',NULL),
(4,'1996-04-13 00:00:00',1,6,2,8,1,6,90,0,NULL,NULL,'\"\"',NULL),
(5,'1996-04-13 00:00:00',1,10,3,7,2,10,90,0,NULL,NULL,'\"\"',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
