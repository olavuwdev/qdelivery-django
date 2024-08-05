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
-- Table structure for table `qdelivery_dados`
--

DROP TABLE IF EXISTS `qdelivery_dados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `qdelivery_dados` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `logo` longtext NOT NULL,
  `icone` longtext NOT NULL,
  `nome` varchar(255) NOT NULL,
  `frete` decimal(10,2) NOT NULL,
  `cnpj` varchar(100) NOT NULL,
  `descricao` longtext NOT NULL,
  `fone` varchar(70) DEFAULT NULL,
  `whatsapp` varchar(70) NOT NULL,
  `email` varchar(255) NOT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `bairro` varchar(255) NOT NULL,
  `cep` varchar(100) NOT NULL,
  `senha_email` varchar(255) NOT NULL,
  `usuario_id` int NOT NULL,
  `ultima_atualizacao` datetime(6) NOT NULL,
  `tipo` varchar(70) DEFAULT NULL,
  `cidade_id` bigint NOT NULL,
  `estado_id` bigint NOT NULL,
  `subtitulo` longtext,
  PRIMARY KEY (`id`),
  KEY `qdelivery_dados_cidade_id_57958435_fk_qdelivery_cidade_id` (`cidade_id`),
  KEY `qdelivery_dados_estado_id_79b37683_fk_qdelivery_estado_id` (`estado_id`),
  KEY `qdelivery_dados_usuario_id_8c34b551` (`usuario_id`),
  CONSTRAINT `qdelivery_dados_cidade_id_57958435_fk_qdelivery_cidade_id` FOREIGN KEY (`cidade_id`) REFERENCES `qdelivery_cidade` (`id`),
  CONSTRAINT `qdelivery_dados_estado_id_79b37683_fk_qdelivery_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `qdelivery_estado` (`id`),
  CONSTRAINT `qdelivery_dados_usuario_id_8c34b551_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qdelivery_dados`
--

LOCK TABLES `qdelivery_dados` WRITE;
/*!40000 ALTER TABLE `qdelivery_dados` DISABLE KEYS */;
INSERT INTO `qdelivery_dados` VALUES (1,'<p><img alt=\"\" src=\"/media/uploads/2024/08/05/quentinhacirgularlogo.png\" style=\"height:500px; width:500px\" /></p>','<p><img alt=\"\" src=\"/media/uploads/2024/08/05/quentinhacirgularlogo_GQaYf0V.png\" style=\"height:500px; width:500px\" /></p>','Quentinha Delivery',2.00,'15.124.512/1212-12','<p>Empresa fundada com proposito de fornecer comida de qualidade e acessivel para a cidade de Mossor&amp;oacute;/RN.Criada em 2023, a <strong>Quentinha Delivery</strong> ate os dias de hoje entrega comida boa e acessivel para todos os clientes.&lt;/p&gt;</p>\r\n\r\n<p>Quem somos?</p>\r\n\r\n<p>Miss&atilde;o</p>\r\n\r\n<p>Valores:</p>','(84)99666-2653','(84)99666-2653','quentinhadelivery0@gmail.com','Rua rio claro',231,'Alto do Sumaré','77.777-777','12345',1,'2024-08-05 16:33:36.629303','ativo',1,1,'<p>Quentinha<strong><span style=\"color:#c0392b\"> Rapida e Deliciosa</span></strong></p>');
/*!40000 ALTER TABLE `qdelivery_dados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-05 17:36:19
