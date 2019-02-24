/*
SQLyog Community v10.3 
MySQL - 5.5.28-log : Database - trapp
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE `mais`;

/*Data for the table `tbl_games` */

insert  into `tbl_games`(`ID`,`MatchTime`,`MatchTypeID`,`HTeamID`,`HScore`,`ATeamID`,`AScore`,`VenueID`,`Duration`,`Attendance`,`Notes`) values (1,'1980-01-01 19:30:00',1,1,3,2,0,1,90,0,'Sample');
insert  into `tbl_games`(`ID`,`MatchTime`,`MatchTypeID`,`HTeamID`,`HScore`,`ATeamID`,`AScore`,`VenueID`,`Duration`,`Attendance`,`Notes`) values (2,'1980-01-08 19:30:00',1,2,0,1,0,2,90,0,'Sample');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
