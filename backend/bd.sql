-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: myproject
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.12.04.1

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add encargado',7,'add_encargado'),(20,'Can change encargado',7,'change_encargado'),(21,'Can delete encargado',7,'delete_encargado'),(22,'Can add empresa',8,'add_empresa'),(23,'Can change empresa',8,'change_empresa'),(24,'Can delete empresa',8,'delete_empresa'),(25,'Can add carreras',9,'add_carreras'),(26,'Can change carreras',9,'change_carreras'),(27,'Can delete carreras',9,'delete_carreras'),(28,'Can add perfil egresado',10,'add_perfilegresado'),(29,'Can change perfil egresado',10,'change_perfilegresado'),(30,'Can delete perfil egresado',10,'delete_perfilegresado'),(31,'Can add datos laborales',11,'add_datoslaborales'),(32,'Can change datos laborales',11,'change_datoslaborales'),(33,'Can delete datos laborales',11,'delete_datoslaborales');
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
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$sFPtWPGe1Pex$Z0dDBYQhpJrD/ej+xSogkV5rPMlPFDAxiZhsbtmj/MQ=','2015-10-27 02:44:52',1,'luis','','','angelito190290@hotmail.com',1,1,'2015-10-27 02:44:05');
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
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
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
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-10-27 05:24:03','1','EVERARDO ABAD ARAGAN',1,'',7,1),(2,'2015-10-27 05:24:08','1','EVERARDO ABAD ARAGAN',1,'',8,1),(3,'2015-10-27 05:24:15','1','EVERARDO',1,'',10,1),(4,'2015-10-27 05:33:33','2','MARICELA',1,'',10,1),(5,'2015-10-27 05:46:23','2','JOSE GREGORIO HERNÁNDEZ DELGADO ',1,'',7,1),(6,'2015-10-27 05:47:22','2','INSTITUTO TECNOLÓGICO DE TEHUACÁN',1,'',8,1),(7,'2015-10-27 05:47:48','3','LUIS CARLOS',1,'',10,1),(8,'2015-10-27 05:49:45','1','2',1,'',11,1),(9,'2015-10-27 05:50:55','2','1',1,'',11,1),(10,'2015-10-27 05:52:09','3','2',1,'',11,1),(11,'2015-10-27 06:04:00','4','ABRAHAM',1,'',10,1),(12,'2015-10-27 06:05:27','4','2',1,'',11,1),(13,'2015-10-27 06:12:54','3','BHR ENTERPRISE WORLDWIDE N',1,'',8,1),(14,'2015-10-27 06:13:31','3','BHR ENTERPRISE WORLDWIDE N',2,'Modifica sector.',8,1),(15,'2015-10-27 06:19:25','4','HSBC MÃ©XICO, S.A. DE C.V.',1,'',8,1),(16,'2015-10-27 06:19:30','5','PATRICIA',1,'',10,1),(17,'2015-10-27 06:21:15','5','1',1,'',11,1),(18,'2015-10-27 06:28:14','6','BEATRIS',1,'',10,1),(19,'2015-10-27 06:29:46','6','4',1,'',11,1),(20,'2015-10-27 06:39:21','4','HSBC MÉXICO, S.A. DE C.V.',2,'Modifica razon_social.',8,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'empresa','empresa'),(7,'empresa','encargado'),(9,'perfil','carreras'),(11,'perfil','datoslaborales'),(10,'perfil','perfilegresado'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-10-27 02:39:47'),(2,'auth','0001_initial','2015-10-27 02:39:49'),(3,'admin','0001_initial','2015-10-27 02:39:49'),(4,'contenttypes','0002_remove_content_type_name','2015-10-27 02:39:50'),(5,'auth','0002_alter_permission_name_max_length','2015-10-27 02:39:50'),(6,'auth','0003_alter_user_email_max_length','2015-10-27 02:39:50'),(7,'auth','0004_alter_user_username_opts','2015-10-27 02:39:51'),(8,'auth','0005_alter_user_last_login_null','2015-10-27 02:39:51'),(9,'auth','0006_require_contenttypes_0002','2015-10-27 02:39:51'),(10,'empresa','0001_initial','2015-10-27 02:39:52'),(11,'perfil','0001_initial','2015-10-27 02:39:53'),(12,'sessions','0001_initial','2015-10-27 02:39:53'),(13,'empresa','0002_auto_20151027_0010','2015-10-27 06:10:32'),(14,'perfil','0002_perfilegresado_municipio','2015-10-27 14:28:28');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xyojaz504wcfg7tba4kcyjjj6xqnebq7','MDQ2NTViZWFjZmExZDlkNDhmODIzZWI3ODEyOWM1ODZlYWI5MTU5YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjMyZGNiNWYxNmM3MDE0MWUwMzc2MWMyMTk1ODEyMTQxZTUzNmVlMGYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-11-10 02:44:52');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa_empresa`
--

DROP TABLE IF EXISTS `empresa_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empresa_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(2) NOT NULL,
  `giro_actividad` varchar(50) DEFAULT NULL,
  `razon_social` varchar(50) NOT NULL,
  `domicilio` varchar(50) DEFAULT NULL,
  `cuidad` varchar(50) DEFAULT NULL,
  `municipio` varchar(50) DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  `e_mail` varchar(254) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `sector` varchar(2) DEFAULT NULL,
  `encargado_id` int(11),
  PRIMARY KEY (`id`),
  KEY `empresa_empresa_572ad821` (`encargado_id`),
  CONSTRAINT `empresa_em_encargado_id_4b049607b13bcbe1_fk_empresa_encargado_id` FOREIGN KEY (`encargado_id`) REFERENCES `empresa_encargado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa_empresa`
--

LOCK TABLES `empresa_empresa` WRITE;
/*!40000 ALTER TABLE `empresa_empresa` DISABLE KEYS */;
INSERT INTO `empresa_empresa` VALUES (1,'2','RESTAURANTE DE COMIDA PARA LLEVAR','EVERARDO ABAD ARAGAN','2DA DE AGUSTIN A. CACHO 15 LOCAL D-E','TEHUACÁN','TEHUACÁN','Puebla','2383831392','','','','33',1),(2,'1','EDUCACIÓN','INSTITUTO TECNOLÓGICO DE TEHUACÁN','LIBRAMIENTO TECNOLÓGICO S/N','TEHUACÁN','TEHUACÁN','Puebla','3822448','','','http://www.ittehuacan.edu.mx','31',2),(3,'2','SERVICIOS PROFESIONALES','BHR ENTERPRISE WORLDWIDE N','','','','Aguascalientes','','','','','11',NULL),(4,'2','INSTITUCIÓN FINANCIERA','HSBC MÉXICO, S.A. DE C.V.','','','','Puebla','','','','','34',NULL);
/*!40000 ALTER TABLE `empresa_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa_encargado`
--

DROP TABLE IF EXISTS `empresa_encargado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empresa_encargado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_encargado` varchar(50) NOT NULL,
  `titulo` varchar(50) DEFAULT NULL,
  `puesto` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa_encargado`
--

LOCK TABLES `empresa_encargado` WRITE;
/*!40000 ALTER TABLE `empresa_encargado` DISABLE KEYS */;
INSERT INTO `empresa_encargado` VALUES (1,'EVERARDO ABAD ARAGAN','CUIDADANO','DUEÑO'),(2,'JOSE GREGORIO HERNÁNDEZ DELGADO ','MAESTRIA EN CIENCIAS','SUBDIRECTOR');
/*!40000 ALTER TABLE `empresa_encargado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_carreras`
--

DROP TABLE IF EXISTS `perfil_carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perfil_carreras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_carrera` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_carreras`
--

LOCK TABLES `perfil_carreras` WRITE;
/*!40000 ALTER TABLE `perfil_carreras` DISABLE KEYS */;
INSERT INTO `perfil_carreras` VALUES (1,'Ing.Bioquimica'),(2,'Ing.Civil'),(3,'Ing. Electronica'),(4,'Ing. Industrial'),(5,'Ing.Mecatronica'),(6,'Ing. Sist. Computacionales'),(7,'Lic. Administración'),(8,'Contaduría Pública'),(9,'Ing. Electromecánica'),(10,'Ing. Gestión Empresarial'),(11,'Ing. Logistica');
/*!40000 ALTER TABLE `perfil_carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_datoslaborales`
--

DROP TABLE IF EXISTS `perfil_datoslaborales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perfil_datoslaborales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medio_obt_trabajo` varchar(2) DEFAULT NULL,
  `req_contratacion` varchar(2) DEFAULT NULL,
  `ant_empleo` varchar(2) DEFAULT NULL,
  `anio_ingr_laboral` datetime NOT NULL,
  `niv_jerarquico` varchar(2) DEFAULT NULL,
  `egresado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `perfil_datoslaborales_9b9d94b8` (`egresado_id`),
  CONSTRAINT `perfil__egresado_id_61659ef21708878c_fk_perfil_perfilegresado_id` FOREIGN KEY (`egresado_id`) REFERENCES `perfil_perfilegresado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_datoslaborales`
--

LOCK TABLES `perfil_datoslaborales` WRITE;
/*!40000 ALTER TABLE `perfil_datoslaborales` DISABLE KEYS */;
INSERT INTO `perfil_datoslaborales` VALUES (1,'2','2','3','2015-10-27 05:49:25','4',1),(2,'1','3','5','2012-01-02 05:50:37','2',2),(3,'2','1','2','1995-01-02 05:51:57','4',3),(4,'2','4','1','2012-01-01 06:05:15','1',4),(5,'1','3','1','2012-01-01 06:21:01','3',5),(6,'4','2','3','2013-01-01 06:29:43','1',6);
/*!40000 ALTER TABLE `perfil_datoslaborales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_perfilegresado`
--

DROP TABLE IF EXISTS `perfil_perfilegresado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perfil_perfilegresado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `a_paterno` varchar(30) NOT NULL,
  `a_materno` varchar(30) NOT NULL,
  `num_control` varchar(9) DEFAULT NULL,
  `f_nacimiento` datetime NOT NULL,
  `sexo` varchar(2) NOT NULL,
  `curp` varchar(19) NOT NULL,
  `e_civil` varchar(2) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `cuidad` varchar(30) NOT NULL,
  `domicilio` varchar(30) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `especialidad` varchar(20) NOT NULL,
  `e_mail` varchar(254) DEFAULT NULL,
  `mes_anio_egreso` datetime NOT NULL,
  `titulado` varchar(2) NOT NULL,
  `ocupacion` varchar(2) NOT NULL,
  `carrera_id` int(11) NOT NULL,
  `empresa_id` int(11) DEFAULT NULL,
  `municipio` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `perfil_perfile_carrera_id_3e47101f3f475127_fk_perfil_carreras_id` (`carrera_id`),
  KEY `perfil_perfile_empresa_id_2af192d891a468e6_fk_empresa_empresa_id` (`empresa_id`),
  CONSTRAINT `perfil_perfile_carrera_id_3e47101f3f475127_fk_perfil_carreras_id` FOREIGN KEY (`carrera_id`) REFERENCES `perfil_carreras` (`id`),
  CONSTRAINT `perfil_perfile_empresa_id_2af192d891a468e6_fk_empresa_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `empresa_empresa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_perfilegresado`
--

LOCK TABLES `perfil_perfilegresado` WRITE;
/*!40000 ALTER TABLE `perfil_perfilegresado` DISABLE KEYS */;
INSERT INTO `perfil_perfilegresado` VALUES (1,'EVERARDO','ABAD','ARAGAN','05360301','1987-06-01 05:19:53','M','AAAE870531HPLBRV14','S','Puebla','TEHUACÁN','9 PONIENTE 103 COLONIA MORELOS','2381337342','IMPUESTOS','eveabadar@gmail.com','2010-12-02 05:21:38','1','4',8,1,'TEHUACAN'),(2,'MARICELA','MONTALVO','PEREZ','04360289','1986-12-24 05:30:34','F','MOPM861223MPLNRR07','C','Puebla','TEHUACÁN','16 DE SEPTIEMBRE 4010 COL OBSE','2381191102','IMPUESTOS','montalvo_perez_m@hotmail.com','2008-12-02 05:32:00','1','1',8,NULL,'TEHUACAN'),(3,'LUIS CARLOS','ORTUÑA','BARBA','88360294','1970-12-21 05:35:50','M','OUBL701220HVZRRS05','C','Puebla','TEHUACÁN','4 ORIENTE 30-C','3838066','IMPUESTOS','lucaorba@yahoo.com','1992-06-02 05:38:39','1','2',8,2,'TEHUACAN'),(4,'ABRAHAM','ROSAS','VIZCAÑO','07360387','1989-03-17 05:54:52','M','ROVA890316HPLSZB07','S','Puebla','CAÑADA MORELOS','NETZAHUALCOYOTL SN COL. LA CRU','249 116 29','IMPUESTOS','lc.abrahamrosas@gmail.com','2011-12-02 05:56:50','2','4',8,NULL,'TEHUACAN'),(5,'PATRICIA','VILLEGAS','CORTOÑA','06360050','1986-08-06 06:15:32','F','VICP860806MPLLRT03','S','Puebla','TEHUACÁN','EL ROSAL NO. 2002 COL. EL EDÉN','2381125843','IMPUESTOS','patricia_villegas_cortes@hotmail.com','2010-06-01 05:17:29','1','1',8,4,'TEHUACAN'),(6,'BEATRIS','DOLORES','TRUJILLO','04360259','1986-08-18 06:25:32','F','DOTB860818MPLLRT05','S','Puebla','TLACOTEPEC DE BENITO JUAREZ','2 SUR NO. 21 SANTA MARIA LA AL','2383908138','IMPUESTOS','bety_dt@hotmail.com','2008-12-01 06:27:29','1','1',8,NULL,'TEHUACAN');
/*!40000 ALTER TABLE `perfil_perfilegresado` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-27  8:49:57
