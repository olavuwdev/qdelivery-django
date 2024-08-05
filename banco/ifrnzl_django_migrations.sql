-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: ifrnzl
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-05 12:35:24.356903'),(2,'auth','0001_initial','2024-08-05 12:35:25.412723'),(3,'admin','0001_initial','2024-08-05 12:35:25.627388'),(4,'admin','0002_logentry_remove_auto_add','2024-08-05 12:35:25.638726'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-05 12:35:25.653540'),(6,'contenttypes','0002_remove_content_type_name','2024-08-05 12:35:25.770361'),(7,'auth','0002_alter_permission_name_max_length','2024-08-05 12:35:25.872365'),(8,'auth','0003_alter_user_email_max_length','2024-08-05 12:35:25.915925'),(9,'auth','0004_alter_user_username_opts','2024-08-05 12:35:25.928917'),(10,'auth','0005_alter_user_last_login_null','2024-08-05 12:35:26.028046'),(11,'auth','0006_require_contenttypes_0002','2024-08-05 12:35:26.031255'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-05 12:35:26.041252'),(13,'auth','0008_alter_user_username_max_length','2024-08-05 12:35:26.152518'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-05 12:35:26.267949'),(15,'auth','0010_alter_group_name_max_length','2024-08-05 12:35:26.298418'),(16,'auth','0011_update_proxy_permissions','2024-08-05 12:35:26.309409'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-05 12:35:26.409863'),(18,'qdelivery','0001_initial','2024-08-05 12:35:26.782911'),(19,'qdelivery','0002_alter_dados_descricao_alter_dados_icone','2024-08-05 12:35:26.898666'),(20,'qdelivery','0003_alter_dados_logo','2024-08-05 12:35:26.991281'),(21,'qdelivery','0004_dados_subtitulo','2024-08-05 12:35:27.023812'),(22,'qdelivery','0005_produtos','2024-08-05 12:35:27.162538'),(23,'qdelivery','0006_produtos_decricao_produtos_valor_alter_dados_usuario','2024-08-05 12:35:27.376468'),(24,'qdelivery','0007_rename_decricao_produtos_descricao','2024-08-05 12:35:27.410060'),(25,'qdelivery','0008_produtos_valor_promo','2024-08-05 12:35:27.443617'),(26,'qdelivery','0009_alter_dados_options','2024-08-05 12:35:27.459461'),(27,'qdelivery','0010_alter_produtos_options','2024-08-05 12:35:27.476548'),(28,'qdelivery','0011_produtos_tipo','2024-08-05 12:35:27.509190'),(29,'qdelivery','0012_alter_produtos_capa','2024-08-05 12:35:27.586357'),(30,'qdelivery','0013_alter_produtos_capa','2024-08-05 12:35:27.600382'),(31,'qdelivery','0014_alter_produtos_options','2024-08-05 12:35:27.613204'),(32,'qdelivery','0015_alter_produtos_options','2024-08-05 12:35:27.628140'),(33,'qdelivery','0016_alter_produtos_tipo','2024-08-05 12:35:27.707416'),(34,'sessions','0001_initial','2024-08-05 12:35:27.755746');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-05 17:36:18
