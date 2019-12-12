/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.5.5-10.1.30-MariaDB : Database - shopdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `detail` */

DROP TABLE IF EXISTS `detail`;

CREATE TABLE `detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `orderid` int(11) unsigned DEFAULT NULL,
  `goodsid` int(11) unsigned DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `detail` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2018-04-08 12:22:15.498037'),(2,'auth','0001_initial','2018-04-08 12:22:15.858037'),(3,'admin','0001_initial','2018-04-08 12:22:15.943037'),(4,'admin','0002_logentry_remove_auto_add','2018-04-08 12:22:15.960537'),(5,'contenttypes','0002_remove_content_type_name','2018-04-08 12:22:16.020537'),(6,'auth','0002_alter_permission_name_max_length','2018-04-08 12:22:16.050537'),(7,'auth','0003_alter_user_email_max_length','2018-04-08 12:22:16.095537'),(8,'auth','0004_alter_user_username_opts','2018-04-08 12:22:16.110537'),(9,'auth','0005_alter_user_last_login_null','2018-04-08 12:22:16.140037'),(10,'auth','0006_require_contenttypes_0002','2018-04-08 12:22:16.147037'),(11,'auth','0007_alter_validators_add_error_messages','2018-04-08 12:22:16.164037'),(12,'auth','0008_alter_user_username_max_length','2018-04-08 12:22:16.241037'),(13,'sessions','0001_initial','2018-04-08 12:22:16.268537');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('1cb6jtq56j9au6d3ifl3r378oiqzluub','ZjhjNTg1MzYwOTYxOWUyODk1NTFlNzJlMGEzYTRlMDU5NTNkYzcyMTp7InZlcmlmeWNvZGUiOiIwMzE0In0=','2018-04-25 06:08:33.951088'),('8i6g2cxek0e732i9dqqu4wx3l30ca42l','MDY5ZjkzNTE1NmRhMTMzMzlkNWQyMmZmZjM5ZGI0NzQ3MjdiMDdhMTp7InZlcmlmeWNvZGUiOiI0MjIxIiwiYWRtaW51c2VyIjp7ImlkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwibmFtZSI6Ilx1N2JhMVx1NzQwNlx1NTQ1ODIiLCJwYXNzd29yZCI6IjIxMjMyZjI5N2E1N2E1YTc0Mzg5NGEwZTRhODAxZmMzIiwiYWRkcmVzcyI6Ilx1NTMxN1x1NGVhY1x1NWUwMlx1NjcxZFx1OTYzM1x1NTMzYVx1NTkyN1x1NWM3MVx1NWI1MDAwN1x1NTNmNyIsInBob25lIjoiMTM1NjY2ODY4NjgiLCJlbWFpbCI6IjEyMjc5NDEwNUBxcS5jb20iLCJzdGF0ZSI6MH19','2018-04-23 06:42:32.449065');

/*Table structure for table `goods` */

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `typeid` int(11) unsigned NOT NULL,
  `goods` varchar(32) NOT NULL,
  `company` varchar(50) DEFAULT NULL,
  `content` text,
  `price` double(6,2) unsigned NOT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `store` int(11) unsigned NOT NULL DEFAULT '0',
  `num` int(11) unsigned NOT NULL DEFAULT '0',
  `clicknum` int(11) unsigned NOT NULL DEFAULT '0',
  `state` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `typeid` (`typeid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `goods` */

insert  into `goods`(`id`,`typeid`,`goods`,`company`,`content`,`price`,`picname`,`store`,`num`,`clicknum`,`state`,`addtime`) values (1,3,'连衣裙','香奈儿','香奈儿的连衣裙',380.00,'1523268599.5389268.jpg',20,0,0,1,'2018-04-09 10:09:59'),(2,6,'联想T4000','联想','      联想T4000              ',3980.00,'1523268691.237927.jpg',10,0,0,1,'2018-04-09 10:11:31'),(3,9,'苹果Iphone 6 S','苹果公司','苹果公司的Iphone 6 S',3680.00,'1523416469.7021515.jpg',28,0,0,2,'2018-04-11 03:14:29'),(4,4,'佳能DS6000','佳能品牌','佳能品牌的单反相机D6000',2880.00,'1523416548.696832.jpg',30,0,0,1,'2018-04-11 03:15:48'),(5,3,'儿童套装','葫芦娃品牌','葫芦娃品牌的儿童套装',120.00,'1523416625.352381.jpg',50,0,0,1,'2018-04-11 03:17:05'),(6,7,'条纹T恤衫','七匹狼','七匹狼的条纹T恤衫',180.00,'1523416690.8561788.jpg',40,0,0,1,'2018-04-11 03:18:10'),(7,3,'红色连衣裙','佰可依品牌','佰可依品牌的红色连衣裙',200.00,'1523416800.3909934.jpg',30,0,0,1,'2018-04-11 03:20:00'),(8,9,'huaweiT2000','华为品牌','华为品牌的huaweiT2000',2300.00,'1523416925.5592127.jpg',50,0,0,1,'2018-04-11 03:22:05'),(9,9,'华为800手机','华为品牌','华为品牌的华为800手机',2680.00,'1523417017.3019178.jpg',30,0,0,1,'2018-04-11 03:23:37'),(10,4,'佳能数码相机','佳能品牌','佳能品牌',800.00,'1523417097.9236016.jpg',30,0,0,2,'2018-04-11 03:24:57'),(11,8,'儿童套装天蓝色','葫芦娃品牌','葫芦娃品牌的儿童套装天蓝色',178.00,'1523417196.8742225.jpg',28,0,0,1,'2018-04-11 03:26:36'),(12,3,'橘黄色连衣裙','GAP品牌','GAP品牌的橘黄色连衣裙',380.00,'1523417307.8867464.jpg',30,0,0,1,'2018-04-11 03:28:27');

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) unsigned DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `total` double(8,2) unsigned DEFAULT NULL,
  `state` tinyint(1) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `orders` */

/*Table structure for table `type` */

DROP TABLE IF EXISTS `type`;

CREATE TABLE `type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) unsigned DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `type` */

insert  into `type`(`id`,`name`,`pid`,`path`) values (1,'服装',0,'0,'),(2,'数码',0,'0,'),(3,'女装',1,'0,1,'),(4,'数码相机',2,'0,2,'),(5,'食品',0,'0,'),(6,'电脑',2,'0,2,'),(7,'男装',1,'0,1,'),(8,'儿童装',1,'0,1,'),(9,'手机',2,'0,2,'),(11,'特色小吃',5,'0,5,');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `password` char(32) NOT NULL,
  `sex` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `state` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`name`,`password`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`) values (1,'admin','管理员2','21232f297a57a5a743894a0e4a801fc3',0,'北京市朝阳区大山子007号','100086','13566686868','122794105@qq.com',0,'2018-04-07 21:20:08'),(3,'zhangsan','张三','e10adc3949ba59abbe56e057f20f883e',1,'北京市三里河蘑菇村102号','100086','12345676890','zhangsan@11.com',0,'2018-04-08 11:11:18'),(4,'lisi','李四','202cb962ac59075b964b07152d234b70',0,'北京市三里河蘑菇村103号','100088','6666666666666','lisi@11.com',2,'2018-04-08 11:12:21'),(6,'wangwu','王五','e10adc3949ba59abbe56e057f20f883e',0,'北京市三里河蘑菇村102号','100086','12345676890','zhangsan@11.com',1,'2018-04-08 12:58:58'),(7,'along','张小龙','202cb962ac59075b964b07152d234b70',1,'北京市海定区上地三街08号嘉华大厦B6-203','100098','12345657890','along@163.com',1,'2018-04-10 07:49:45'),(8,'caihua','菜花','202cb962ac59075b964b07152d234b70',0,'北京市宣武区菜市口100号新龙小区3#-2-608','100036','1234567890','caihua@126.com',1,'2018-04-10 07:51:27'),(9,'huangsan','黄三','202cb962ac59075b964b07152d234b70',1,'北京市昌平区回龙观流星花园A6-3-403','100082','13456767867','huansan@sohu.com',1,'2018-04-10 07:53:18'),(10,'aidehua','爱德华','202cb962ac59075b964b07152d234b70',1,'北京市宣武区菜市口100号新龙小区3#-2-608','100088','12345657890','zhangsan@qq.com',1,'2018-04-10 07:54:42'),(11,'wangnan','王楠','202cb962ac59075b964b07152d234b70',1,'北京市宣武区菜市口100号新龙小区3#-2-608','100088','12345657890','wangnan@180.com',1,'2018-04-10 07:55:39'),(12,'zhangle','张乐','202cb962ac59075b964b07152d234b70',0,'北京市海定区上地三街08号嘉华大厦B6-203','100086','12345657890','zhangle@126.com',1,'2018-04-10 07:56:36'),(13,'wangsheng','王胜','202cb962ac59075b964b07152d234b70',1,'北京市三里河蘑菇村102号','100088','33333333333','wangsheng@163.com',1,'2018-04-10 07:57:27'),(14,'xusheng','徐盛','202cb962ac59075b964b07152d234b70',1,'北京市三里河蘑菇村103号','100088','12345657890','xusheng@122.com',1,'2018-04-10 07:58:15'),(15,'xumo','许墨','202cb962ac59075b964b07152d234b70',0,'北京市三里河蘑菇村103号','100088','12345657890','xumo@136.com',1,'2018-04-10 07:59:32'),(16,'zhangmo','张墨','202cb962ac59075b964b07152d234b70',1,'北京市海定区上地三街08号嘉华大厦B6-203','100086','12345324678','zhangmo@163.com',1,'2018-04-10 08:00:21'),(17,'zhangjun','张军','202cb962ac59075b964b07152d234b70',0,'北京市宣武区菜市口100号新龙小区3#-2-608','100086','12345657890','zhangjun@163.com',1,'2018-04-10 08:01:06');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
