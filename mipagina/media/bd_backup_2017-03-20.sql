-- MySQL dump 10.13  Distrib 5.6.25, for Win32 (x86)
--
-- Host: localhost    Database: almacenAnterior
-- ------------------------------------------------------
-- Server version	5.6.25

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add perfiles',7,'add_perfiles'),(20,'Can change perfiles',7,'change_perfiles'),(21,'Can delete perfiles',7,'delete_perfiles'),(22,'Can add trabajador',8,'add_trabajador'),(23,'Can change trabajador',8,'change_trabajador'),(24,'Can delete trabajador',8,'delete_trabajador'),(25,'Can add categoria',9,'add_categoria'),(26,'Can change categoria',9,'change_categoria'),(27,'Can delete categoria',9,'delete_categoria'),(28,'Can add producto',10,'add_producto'),(29,'Can change producto',10,'change_producto'),(30,'Can delete producto',10,'delete_producto'),(31,'Can add compra producto',11,'add_compraproducto'),(32,'Can change compra producto',11,'change_compraproducto'),(33,'Can delete compra producto',11,'delete_compraproducto'),(34,'Can add salidas pro',12,'add_salidaspro'),(35,'Can change salidas pro',12,'change_salidaspro'),(36,'Can delete salidas pro',12,'delete_salidaspro'),(37,'Can add proveedor',13,'add_proveedor'),(38,'Can change proveedor',13,'change_proveedor'),(39,'Can delete proveedor',13,'delete_proveedor'),(40,'Can add reserva',14,'add_reserva'),(41,'Can change reserva',14,'change_reserva'),(42,'Can delete reserva',14,'delete_reserva');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$qbTOkjp7eyxR$sNo/YDJHmhVR85CywuZ5ewpP1uWJuOhOkbxmhnxgk44=','2017-03-20 20:06:04',1,'beimar','beimar','beimar','beimar@gmail.com',1,1,'2017-02-24 13:43:50');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_trabajador`
--

DROP TABLE IF EXISTS `cliente_trabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_trabajador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_trabajador` varchar(150) NOT NULL,
  `Apellidos` varchar(150) NOT NULL,
  `Ci_Nit` int(10) unsigned NOT NULL,
  `Telefono` int(10) unsigned NOT NULL,
  `Email` varchar(75) NOT NULL,
  `Direccion` varchar(150) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Ci_Nit` (`Ci_Nit`),
  UNIQUE KEY `Telefono` (`Telefono`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_trabajador`
--

LOCK TABLES `cliente_trabajador` WRITE;
/*!40000 ALTER TABLE `cliente_trabajador` DISABLE KEYS */;
INSERT INTO `cliente_trabajador` VALUES (1,'jhose','jhose',454545,65986598,'jhose@hotmail.com','La Paz','2017-02-25 19:24:28',0),(2,'felipe','felipe',789654,78454851,'felipe@gmail.com','linares','2017-03-20 16:34:36',0);
/*!40000 ALTER TABLE `cliente_trabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-03-14 19:09:02','1','juan',1,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'perfiles','inicio','perfiles'),(8,'trabajador','cliente','trabajador'),(9,'categoria','producto','categoria'),(10,'producto','producto','producto'),(11,'compra producto','producto','compraproducto'),(12,'salidas pro','producto','salidaspro'),(13,'proveedor','proveedor','proveedor'),(14,'reserva','producto','reserva');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-02-24 13:42:57'),(2,'auth','0001_initial','2017-02-24 13:43:15'),(3,'admin','0001_initial','2017-02-24 13:43:19'),(4,'sessions','0001_initial','2017-02-24 13:43:20'),(5,'producto','0001_initial','2017-03-11 02:34:25'),(6,'producto','0002_reserva','2017-03-11 02:54:44'),(7,'producto','0003_auto_20170311_0616','2017-03-11 13:17:00'),(8,'producto','0004_reserva_fecha','2017-03-13 14:13:40'),(9,'producto','0005_auto_20170320_1336','2017-03-20 20:36:34');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('vybzaxzh8sqzhpnejj0v46pfq6c3kkfg','ZmUwNjkxYTAzYmI1NWZhZDZiZGM1OWNiZDY4NDZmYTNiNzBjMmI5Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImJkNTUzMWFjZmZjYTc1MzE4Yzc3NzdlODQ2ZjY3YzBhN2JhZmVlNzUiLCJfYXV0aF91c2VyX2lkIjoxLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImNhcnJpdG8iOltdLCJyZXNlcnZhIjpbXSwiaW5ncmVzbyI6W119','2017-04-03 20:06:04'),('wtewn5bctewia47balb30cx1sml4tyqs','ZTczZTI2MGIyMDczZmM2OGZjNmY5NGM4OTZiNWNmNTBhODdkNjJkMDp7Il9hdXRoX3VzZXJfaGFzaCI6ImFhZGZmNWVkZDIwZTJmMTQ5NTY4ZGQ4MzY5ZWE0Yjg1MDg0NTMxNmMiLCJfYXV0aF91c2VyX2lkIjoxLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsImNhcnJpdG8iOltdLCJyZXNlcnZhIjpbXSwiaW5ncmVzbyI6W119','2017-03-29 19:22:08');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inicio_perfiles`
--

DROP TABLE IF EXISTS `inicio_perfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inicio_perfiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `ci` int(11) NOT NULL,
  `telefono` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inicio_perfiles`
--

LOCK TABLES `inicio_perfiles` WRITE;
/*!40000 ALTER TABLE `inicio_perfiles` DISABLE KEYS */;
INSERT INTO `inicio_perfiles` VALUES (1,1,8554932,71837376);
/*!40000 ALTER TABLE `inicio_perfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_categoria`
--

DROP TABLE IF EXISTS `producto_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_categoria` varchar(50) NOT NULL,
  `Material` varchar(50) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre_categoria` (`Nombre_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_categoria`
--

LOCK TABLES `producto_categoria` WRITE;
/*!40000 ALTER TABLE `producto_categoria` DISABLE KEYS */;
INSERT INTO `producto_categoria` VALUES (1,'Material de Oficina','Artículo','2017-02-25 19:22:52',0);
/*!40000 ALTER TABLE `producto_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_compraproducto`
--

DROP TABLE IF EXISTS `producto_compraproducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_compraproducto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Precio_unidad` double NOT NULL,
  `cantidad` int(10) unsigned NOT NULL,
  `producto_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  `total` double NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_compraproducto_1635d9bd` (`producto_id`),
  KEY `producto_compraproducto_0e63be46` (`proveedor_id`),
  CONSTRAINT `producto_id_refs_id_818fbfb8` FOREIGN KEY (`producto_id`) REFERENCES `producto_producto` (`id`),
  CONSTRAINT `proveedor_id_refs_id_075b4ac3` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor_proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_compraproducto`
--

LOCK TABLES `producto_compraproducto` WRITE;
/*!40000 ALTER TABLE `producto_compraproducto` DISABLE KEYS */;
INSERT INTO `producto_compraproducto` VALUES (1,2500,10,1,1,25000,'2017-02-25 19:31:09',0),(2,2500,4,1,1,10000,'2017-02-25 20:11:07',0),(3,45,2,2,1,90,'2017-03-15 01:12:37',0),(4,45,2,2,1,90,'2017-03-15 01:20:33',0),(5,45,1,2,1,45,'2017-03-15 01:28:31',0),(6,45,1,2,1,45,'2017-03-15 01:30:55',0);
/*!40000 ALTER TABLE `producto_compraproducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_producto`
--

DROP TABLE IF EXISTS `producto_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_producto` varchar(150) NOT NULL,
  `Marca` varchar(50) NOT NULL,
  `Precio_producto` double NOT NULL,
  `Stock` int(11) NOT NULL,
  `Usuario_id` int(11) NOT NULL,
  `Categoria_id` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  `archivo` varchar(100),
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre_producto` (`Nombre_producto`),
  KEY `producto_producto_abe53167` (`Usuario_id`),
  KEY `producto_producto_57ce68aa` (`Categoria_id`),
  CONSTRAINT `Categoria_id_refs_id_92a461f4` FOREIGN KEY (`Categoria_id`) REFERENCES `producto_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_producto`
--

LOCK TABLES `producto_producto` WRITE;
/*!40000 ALTER TABLE `producto_producto` DISABLE KEYS */;
INSERT INTO `producto_producto` VALUES (1,'Computadora','HP',2500,2,1,1,'2017-02-25 19:25:42',0,'productos/abrasame_OqYPQCP.jpg'),(2,'Calculadora','Hp',45,4,1,1,'2017-03-08 18:41:53',0,'productos/abrasame_t0Qfr2R.jpg'),(3,'Teclados','Dell',45,0,1,1,'2017-03-15 19:23:47',0,'productos/FB_IMG_14895229570925627.jpg'),(4,'Mesas','Roble',450,0,1,1,'2017-03-15 19:25:55',0,'productos/FB_IMG_14895229446661060.jpg'),(5,'Roperos','Roble',800,0,1,1,'2017-03-15 19:27:16',1,'productos/FB_IMG_14895224715336116.jpg'),(6,'Aceites','Aceite',80,0,1,1,'2017-03-15 19:28:16',0,'productos/FB_IMG_14895224963961269.jpg'),(7,'Cuadertos','Lider',10,0,1,1,'2017-03-15 19:29:12',0,'productos/FB_IMG_14895230411882931.jpg'),(8,'celular','sony',850,0,1,1,'2017-03-20 20:37:13',0,'');
/*!40000 ALTER TABLE `producto_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_reserva`
--

DROP TABLE IF EXISTS `producto_reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_reserva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Total` int(10) unsigned,
  `cantidad` int(10) unsigned NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `id_trabajador_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `adelanto` int(10) unsigned NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_reserva_e86587dc` (`id_trabajador_id`),
  KEY `producto_reserva_bb91903a` (`producto_id`),
  CONSTRAINT `producto_reser_id_trabajador_id_9552166_fk_cliente_trabajador_id` FOREIGN KEY (`id_trabajador_id`) REFERENCES `cliente_trabajador` (`id`),
  CONSTRAINT `producto_reserva_producto_id_3378d9f_fk_producto_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto_producto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_reserva`
--

LOCK TABLES `producto_reserva` WRITE;
/*!40000 ALTER TABLE `producto_reserva` DISABLE KEYS */;
INSERT INTO `producto_reserva` VALUES (1,5000,2,'2017-03-11 13:33:31',1,1,1,2500,'2015-05-01'),(2,10000,4,'2017-03-11 13:46:04',1,1,1,5000,'2015-05-05'),(3,10000,4,'2017-03-11 15:09:35',1,1,1,2000,'2015-05-05'),(4,10000,4,'2017-03-11 15:19:39',1,1,1,300,'2015-05-05'),(5,10000,4,'2017-03-11 15:39:06',0,1,1,3000,'2015-05-05'),(6,2500,1,'2017-03-11 15:43:43',1,1,1,45,'2015-05-05'),(7,10000,4,'2017-03-13 14:29:18',0,1,1,1500,'2017-03-17'),(8,45,1,'2017-03-13 14:30:57',1,1,2,40,'2015-05-05'),(9,90,2,'2017-03-20 17:01:44',1,1,2,20,'2017-03-15'),(10,900,2,'2017-03-20 19:40:45',1,1,4,0,'2017-03-27'),(11,90,2,'2017-03-20 19:42:03',1,1,3,0,'2017-03-27');
/*!40000 ALTER TABLE `producto_reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_salidaspro`
--

DROP TABLE IF EXISTS `producto_salidaspro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto_salidaspro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Precio_unidad` double NOT NULL,
  `cantidad` int(10) unsigned NOT NULL,
  `producto_id` int(11) NOT NULL,
  `total` double NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `producto_salidaspro_1635d9bd` (`producto_id`),
  KEY `producto_salidaspro_061b2772` (`trabajador_id`),
  CONSTRAINT `producto_id_refs_id_83e36000` FOREIGN KEY (`producto_id`) REFERENCES `producto_producto` (`id`),
  CONSTRAINT `trabajador_id_refs_id_e627d114` FOREIGN KEY (`trabajador_id`) REFERENCES `cliente_trabajador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_salidaspro`
--

LOCK TABLES `producto_salidaspro` WRITE;
/*!40000 ALTER TABLE `producto_salidaspro` DISABLE KEYS */;
INSERT INTO `producto_salidaspro` VALUES (1,2500,4,1,10000,1,'2017-02-25 20:10:19',0),(2,2500,2,1,5000,1,'2017-02-25 20:51:25',0),(3,2500,2,1,5000,1,'2017-02-25 21:01:34',0),(4,2500,2,1,5000,1,'2017-03-11 15:30:17',0),(5,2500,1,1,2500,1,'2017-03-14 19:37:30',0),(6,45,1,2,45,1,'2017-03-15 01:25:12',0),(7,45,1,2,45,1,'2017-03-15 01:26:12',0),(8,2500,1,1,2500,1,'2017-03-15 01:31:46',0);
/*!40000 ALTER TABLE `producto_salidaspro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor_proveedor`
--

DROP TABLE IF EXISTS `proveedor_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedor_proveedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_Razon_Social` varchar(200) NOT NULL,
  `Nit` int(10) unsigned NOT NULL,
  `Telefono` int(10) unsigned NOT NULL,
  `Direccion` varchar(150) NOT NULL,
  `Email` varchar(75) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Nombre_Razon_Social` (`Nombre_Razon_Social`),
  UNIQUE KEY `Nit` (`Nit`),
  UNIQUE KEY `Telefono` (`Telefono`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor_proveedor`
--

LOCK TABLES `proveedor_proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor_proveedor` DISABLE KEYS */;
INSERT INTO `proveedor_proveedor` VALUES (1,'luis',2443434,78457845,'bustillos','luis@gmail.com','2017-02-25 19:23:36',0);
/*!40000 ALTER TABLE `proveedor_proveedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-20 13:40:58
