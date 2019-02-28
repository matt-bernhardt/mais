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

/*Data for the table `lkp_matchtypes` */

insert  into `lkp_matchtypes`(`MatchType`,`id`,`Official`,`CompetitionType`,`Abbv`) values 
('MLS League',21,1,'League','mls'),
('USL League',27,1,'League','usl'),
('NASL League',28,1,'League','nasl');

/*Data for the table `tbl_games` */

insert  into `tbl_games`(`ID`,`MatchTime`,`MatchTypeID`,`HteamID`,`Hscore`,`AteamID`,`Ascore`,`VenueID`,`Duration`,`Attendance`,`MeanTemperature`,`Precipitation`,`WeatherEvents`,`Notes`) values 
(1,'1996-04-06 00:00:00',21,9,1,3,0,9,90,0,NULL,NULL,'\"\"',NULL),
(2,'1996-04-13 00:00:00',21,2,4,3,0,2,90,0,NULL,NULL,'\"\"',NULL),
(3,'1996-04-13 00:00:00',21,5,3,1,0,5,90,0,NULL,NULL,'\"\"',NULL),
(6,'1996-04-14 00:00:00',21,3,1,9,0,3,90,0,NULL,NULL,'\"\"',NULL),
(4,'1996-04-13 00:00:00',21,6,2,8,1,6,90,0,NULL,NULL,'\"\"',NULL),
(5,'1996-04-13 00:00:00',21,10,3,7,2,10,90,0,NULL,NULL,'\"\"',NULL);

/*Data for the table `tbl_teams` */

insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (1,'Colorado Rapids','COL');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (2,'Columbus Crew','CLB');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (3,'D.C. United','DC');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (4,'Dallas Burn','DAL');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (5,'Kansas City Wiz','KC');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (6,'Los Angeles Galaxy','LA');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (7,'New England Revolution','NE');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (8,'NY/NJ Metrostars','NY');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (9,'San Jose Clash','SJ');
insert  into `tbl_teams`(`ID`,`teamname`,`team3ltr`) values (10,'Tampa Bay Mutiny','TB');


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
