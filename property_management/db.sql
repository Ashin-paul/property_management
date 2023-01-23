/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.14-MariaDB : Database - py_property_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`py_property_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `py_property_management`;

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`) values (1,'mmm'),(2,'aaa'),(3,'juol'),(4,'hsjsjk'),(5,'erty');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`reply`,`date_time`) values (1,1,'hiii','hello','2'),(2,1,'koiii','reply-pending','2022-03-09'),(3,1,'ghj','reply-pending','2022-03-09 13:01:49');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'alen','alen','user'),(2,'admin','admin','admin'),(3,'jo','jo','user'),(4,'alen','alen','user'),(5,'alen','alen','user');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `message` */

insert  into `message`(`message_id`,`sender_id`,`receiver_id`,`message`,`date_time`) values (1,2,1,'hi','2022-03-10 09:59:05'),(2,1,2,'hello','2022-03-10 09:59:17'),(3,2,1,'sugamano?','2022-03-10 10:25:28'),(4,1,1,'hi','2022-03-10 15:23:29'),(5,1,2,'sugam','2022-03-10 15:33:33'),(6,1,2,'hai','2022-03-10 15:38:33'),(7,1,2,'hello','2022-03-10 15:38:38'),(8,2,1,'hii','2022-03-10 15:39:40'),(9,2,1,'hekfkf','2022-03-10 15:39:50'),(10,2,1,'heeee','2022-03-10 15:40:11'),(11,2,1,'mmmm','2022-03-10 15:40:16'),(12,2,1,'gyuhh','2022-03-10 15:40:23'),(13,2,1,'koii','2022-03-10 15:40:38'),(14,2,1,'oiiii','2022-03-10 15:40:43'),(15,2,1,'pokmn','2022-03-10 15:45:32'),(16,2,1,'kkk','2022-03-10 16:46:33');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`request_id`,`amount`,`date`) values (1,1,'50000','2022-03-09');

/*Table structure for table `property` */

DROP TABLE IF EXISTS `property`;

CREATE TABLE `property` (
  `property_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `property_title` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`property_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `property` */

insert  into `property`(`property_id`,`user_id`,`category_id`,`property_title`,`amount`,`description`,`date_time`,`status`) values (1,1,2,'lop','50000','jioplggu jnbhjhuu','2022-03-09 11:54:54','pending');

/*Table structure for table `property_images` */

DROP TABLE IF EXISTS `property_images`;

CREATE TABLE `property_images` (
  `property_image_id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`property_image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `property_images` */

insert  into `property_images`(`property_image_id`,`property_id`,`image`) values (1,1,'static/assets/imgc8877326-8cd4-469e-b4b2-defb43193fcapexels-binyamin-mellish-1396132.jpg'),(2,1,'static/assets/img163f0fa7-0730-4596-b68c-8fbdf5f01793chris-orcutt-DmEX6_oQI-U-unsplash.jpg'),(3,1,'static/assets/imgf044a019-cf64-4ca8-a618-648f3c8ee751pexels-alex-staudinger-1732414.jpg'),(4,1,'static/assets/imgb794a447-d878-474f-962b-c96df54c794ddownload.jpg');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `property_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`property_id`,`amount`,`date_time`,`status`) values (1,1,1,'50000','2022-03-09 21:47:17','pending'),(6,2,1,'50000','2022-03-10 09:29:05','pending');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `housename` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`firstname`,`lastname`,`housename`,`place`,`pincode`,`phone`,`email`) values (1,1,'ALEN','LAWERENCE','VILLA','THRISSUR','682007','8811223344','alen12@gmail.com'),(2,3,'joel','thomas','josvilla','kochi','682574','9988776611','jo@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
