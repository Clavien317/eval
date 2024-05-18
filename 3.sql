-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 18 mai 2024 à 09:08
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `3`
--

-- --------------------------------------------------------

--
-- Structure de la table `resultat_examen`
--

DROP TABLE IF EXISTS `resultat_examen`;
CREATE TABLE IF NOT EXISTS `resultat_examen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `note` int NOT NULL,
  `code_matiere` varchar(10) NOT NULL,
  `niveau` varchar(10) NOT NULL DEFAULT 'L1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `resultat_examen`
--

INSERT INTO `resultat_examen` (`id`, `note`, `code_matiere`, `niveau`) VALUES
(1, 12, 'ALG', 'L2'),
(2, 9, 'ALG', 'L1'),
(3, 12, 'ALG', 'M1'),
(4, 12, 'ALG', 'L1'),
(5, 4, 'ALG', 'L1'),
(6, 4, 'ALG', 'L1'),
(7, 4, 'ALG', 'L1'),
(8, 4, 'ALG', 'L1'),
(9, 14, 'ALG', 'L3'),
(10, 14, 'ALG', 'M2'),
(11, 10, 'ALG', 'M1');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
