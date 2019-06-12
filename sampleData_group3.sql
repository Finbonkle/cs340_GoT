-- Group 3
-- Michelle Thuong Huynh
-- James Tyler Ball

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: classmysql.engr.oregonstate.edu:3306
-- Generation Time: May 05, 2019 at 07:51 PM
-- Server version: 10.3.13-MariaDB-log
-- PHP Version: 7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_huynhthu`
--

-- --------------------------------------------------------

--
-- Table structure for table `bsg_cert`
--

CREATE TABLE `bsg_cert` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bsg_cert`
--

INSERT INTO `bsg_cert` (`id`, `title`) VALUES
(1, 'Raptor'),
(2, 'Viper'),
(3, 'Mechanic'),
(4, 'Command');

-- --------------------------------------------------------

--
-- Table structure for table `bsg_cert_people`
--

CREATE TABLE `bsg_cert_people` (
  `cid` int(11) NOT NULL DEFAULT 0,
  `pid` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bsg_cert_people`
--

INSERT INTO `bsg_cert_people` (`cid`, `pid`) VALUES
(1, 7),
(2, 2),
(2, 4),
(3, 8),
(3, 9),
(4, 2),
(4, 3),
(4, 6);

-- --------------------------------------------------------

--
-- Table structure for table `bsg_people`
--

CREATE TABLE `bsg_people` (
  `id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) DEFAULT NULL,
  `homeworld` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bsg_people`
--

INSERT INTO `bsg_people` (`id`, `fname`, `lname`, `homeworld`, `age`) VALUES
(1, 'William', 'Adama', 3, 61),
(2, 'Lee', 'Adama', 3, 30),
(3, 'Laura', 'Roslin', 3, NULL),
(4, 'Kara', 'Thrace', 3, NULL),
(5, 'Gaius', 'Baltar', 3, NULL),
(6, 'Saul', 'Tigh', NULL, 71),
(7, 'Karl', 'Agathon', 1, NULL),
(8, 'Galen', 'Tyrol', 1, 32),
(9, 'Callandra', 'Henderson', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bsg_people_copy`
--

CREATE TABLE `bsg_people_copy` (
  `id` int(11) NOT NULL DEFAULT 0,
  `fname` varchar(255) CHARACTER SET latin1 NOT NULL,
  `lname` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `homeworld` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bsg_people_copy`
--

INSERT INTO `bsg_people_copy` (`id`, `fname`, `lname`, `homeworld`, `age`) VALUES
(1, 'William', 'Adama', 3, 61),
(2, 'Lee', 'Adama', 3, 30),
(3, 'Laura', 'Roslin', 3, NULL),
(4, 'Kara', 'Thrace', 3, NULL),
(5, 'Gaius', 'Baltar', 3, NULL),
(6, 'Saul', 'Tigh', NULL, 71),
(7, 'Karl', 'Agathon', 1, NULL),
(8, 'Galen', 'Tyrol', 1, 32),
(9, 'Callandra', 'Henderson', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bsg_planets`
--

CREATE TABLE `bsg_planets` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `population` bigint(20) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `capital` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bsg_planets`
--

INSERT INTO `bsg_planets` (`id`, `name`, `population`, `language`, `capital`) VALUES
(1, 'Gemenon', 2800000000, 'Old Gemenese', 'Oranu'),
(2, 'Leonis', 2600000000, 'Leonese', 'Luminere'),
(3, 'Caprica', 4900000000, 'Caprican', 'Caprica City'),
(7, 'Sagittaron', 1700000000, NULL, 'Tawa'),
(16, 'Aquaria', 25000, NULL, NULL),
(17, 'Canceron', 6700000000, NULL, 'Hades'),
(18, 'Libran', 2100000, NULL, NULL),
(19, 'Picon', 1400000000, NULL, 'Queestown'),
(20, 'Scorpia', 450000000, NULL, 'Celeste'),
(21, 'Tauron', 2500000000, 'Tauron', 'Hypatia'),
(22, 'Virgon', 4300000000, NULL, 'Boskirk');

-- --------------------------------------------------------

--
-- Table structure for table `Characters`
--

CREATE TABLE `Characters` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `alive` tinyint(1) DEFAULT NULL,
  `mannerOfDeath` varchar(255) DEFAULT NULL,
  `portrayal` varchar(255) DEFAULT NULL,
  `phil_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Characters`
--

INSERT INTO `Characters` (`id`, `name`, `alive`, `mannerOfDeath`, `portrayal`, `phil_id`) VALUES
(1, 'Jaime Lannister', 1, NULL, 'Nikolaj Coster-Waldau', NULL),
(2, 'Cersei Lannister', 1, NULL, 'Lena Headey', NULL),
(3, 'Daenerys Targaryen', 1, NULL, 'Emilia Clarke', NULL),
(4, 'Jorah Mormont', 0, 'Stabbed multiple times by wights', 'Iain Glen', 1),
(5, 'Jon Snow', 1, NULL, 'Kit Harington', 1),
(6, 'Sansa Stark', 1, NULL, 'Sophie Turner', 2),
(7, 'Arya Stark', 1, NULL, 'Maisie Williams', 3),
(8, 'Theon Greyjoy', 0, 'Impaled with a broken spear by the Night King', 'Alfie Allen', 4);

-- --------------------------------------------------------

--
-- Table structure for table `diagnostic`
--

CREATE TABLE `diagnostic` (
  `id` int(11) NOT NULL,
  `text` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `diagnostic`
--

INSERT INTO `diagnostic` (`id`, `text`) VALUES
(1, 'MySQL is Working!');

-- --------------------------------------------------------

--
-- Table structure for table `Factions`
--

CREATE TABLE `Factions` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `strength` varchar(255) DEFAULT NULL,
  `weakness` varchar(255) DEFAULT NULL,
  `phil_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Factions`
--

INSERT INTO `Factions` (`id`, `name`, `type`, `strength`, `weakness`, `phil_id`) VALUES
(1, 'Lannisters', 'House', 'Wealth', 'Pride', 2),
(2, 'Targaryens', 'House', 'Dragons', 'Lack of Resources', 2),
(3, 'Mormonts', 'House', 'Effective Tactics', 'Underhanded Tactics', 1),
(4, 'Greyjoys', 'House', 'Sailing', 'Need for Conquest', 4),
(5, 'Faceless Men', 'Cult', 'Magic', 'Small Numbers', 3),
(6, 'Brotherhood without Banners', 'Militia', 'Loyalty', 'Lack of Purpose', 4),
(7, 'Starks', 'House', 'Knowledge of Winter', 'Honor', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Factions_Characters`
--

CREATE TABLE `Factions_Characters` (
  `fact_id` int(11) NOT NULL,
  `char_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Factions_Characters`
--

INSERT INTO `Factions_Characters` (`fact_id`, `char_id`) VALUES
(1, NULL),
(2, NULL),
(3, NULL),
(4, NULL),
(5, NULL),
(6, NULL),
(7, NULL),
(1, 1),
(1, 2),
(2, 3),
(2, 5),
(3, 4),
(4, 8),
(5, 7),
(7, 5),
(7, 6),
(7, 7),
(7, 8);

-- --------------------------------------------------------

--
-- Table structure for table `Philosophies`
--

CREATE TABLE `Philosophies` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `supernatural` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Philosophies`
--

INSERT INTO `Philosophies` (`id`, `name`, `type`, `supernatural`) VALUES
(1, 'Old Gods of the Forest', 'Polytheistic', 1),
(2, 'Faith of the Seven', 'Polytheistic', 0),
(3, 'Many-Faced God', 'Monotheistic', 1),
(4, 'Drowned God', 'Monotheistic', 0),
(5, 'Lord of Light', 'Monotheistic', 1);

-- --------------------------------------------------------


--
-- Table structure for table `Seasons`
--

CREATE TABLE `Seasons` (
  `id` int(11) NOT NULL,
  `char_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Seasons`
--

INSERT INTO `Seasons` (`id`, `char_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(2, 3),
(3, 1),
(3, 2),
(3, 3),
(4, 1),
(4, 2),
(4, 3),
(5, 1),
(5, 2),
(5, 3),
(6, 1),
(6, 2),
(6, 3),
(7, 1),
(7, 2),
(7, 3),
(8, 1),
(8, 2),
(8, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bsg_cert`
--
ALTER TABLE `bsg_cert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bsg_cert_people`
--
ALTER TABLE `bsg_cert_people`
  ADD PRIMARY KEY (`cid`,`pid`),
  ADD KEY `pid` (`pid`);

--
-- Indexes for table `bsg_people`
--
ALTER TABLE `bsg_people`
  ADD PRIMARY KEY (`id`),
  ADD KEY `homeworld` (`homeworld`);

--
-- Indexes for table `bsg_planets`
--
ALTER TABLE `bsg_planets`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `Characters`
--
ALTER TABLE `Characters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `char_phil_id` (`phil_id`);

--
-- Indexes for table `diagnostic`
--
ALTER TABLE `diagnostic`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Factions`
--
ALTER TABLE `Factions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `phil_id` (`phil_id`);


--
-- Indexes for table `Factions_Characters`
--
ALTER TABLE `Factions_Characters`
  ADD PRIMARY KEY (`fact_id`,`char_id`),
  ADD KEY `fact_char_id` (`char_id`);

--
-- Indexes for table `Philosophies`
--
ALTER TABLE `Philosophies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Seasons`
--
ALTER TABLE `Seasons`
  ADD PRIMARY KEY (`id`,`char_id`),
  ADD KEY `char_id` (`char_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bsg_cert`
--
ALTER TABLE `bsg_cert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `bsg_people`
--
ALTER TABLE `bsg_people`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `bsg_planets`
--
ALTER TABLE `bsg_planets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `Characters`
--
ALTER TABLE `Characters`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `diagnostic`
--
ALTER TABLE `diagnostic`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Factions`
--
ALTER TABLE `Factions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Philosophies`
--
ALTER TABLE `Philosophies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bsg_cert_people`
--
ALTER TABLE `bsg_cert_people`
  ADD CONSTRAINT `bsg_cert_people_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `bsg_cert` (`id`),
  ADD CONSTRAINT `bsg_cert_people_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `bsg_people` (`id`);

--
-- Constraints for table `bsg_people`
--
ALTER TABLE `bsg_people`
  ADD CONSTRAINT `bsg_people_ibfk_1` FOREIGN KEY (`homeworld`) REFERENCES `bsg_planets` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Characters`
--
ALTER TABLE `Characters`
  ADD CONSTRAINT `char_phil_id` FOREIGN KEY (`phil_id`) REFERENCES `Philosophies` (`id`);

--
-- Constraints for table `Factions`
--
ALTER TABLE `Factions`
  ADD CONSTRAINT `phil_id` FOREIGN KEY (`phil_id`) REFERENCES `Philosophies` (`id`);

/*
--
-- Constraints for table `Factions_Characters`
--
ALTER TABLE `Factions_Characters`
  ADD CONSTRAINT `fact_char_id` FOREIGN KEY (`char_id`) REFERENCES `Characters` (`id`),
  ADD CONSTRAINT `fact_id` FOREIGN KEY (`fact_id`) REFERENCES `Factions` (`id`);


--
-- Constraints for table `Seasons`
--
ALTER TABLE `Seasons`
  ADD CONSTRAINT `char_id` FOREIGN KEY (`char_id`) REFERENCES `Characters` (`id`);
COMMIT;
*/


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
