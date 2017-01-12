CREATE DATABASE IF NOT EXISTS `lab2films` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lab2films`;

CREATE TABLE IF NOT EXISTS `actors` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `language` varchar(100) NOT NULL,
  `birth_year` year(4) NOT NULL,
  `ganre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

INSERT INTO `actors` (`id`, `name`, `country`, `language`, `birth_year`, `ganre`) VALUES
	(1, 'Actress', 'Country3', 'Language1', 1994, 'Ganre1'),
	(2, 'Actor2', 'Country2', 'Language1', 1980, 'Ganre2'),
	(3, 'Actor3', 'Country3', 'Language2', 2000, 'Ganre3'),
	(4, 'Actor4', 'Country1', 'Language1', 1994, 'Ganre1'),
	(6, 'Actor5', 'Country3', 'Language2', 1999, 'Ganre2');

CREATE TABLE IF NOT EXISTS `directors` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `birth_year` year(4) NOT NULL,
  `country` varchar(100) NOT NULL,
  `ganre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

INSERT INTO `directors` (`id`, `name`, `birth_year`, `country`, `ganre`) VALUES
	(1, 'Director1', 1993, 'Country1', 'Ganre2'),
	(2, 'Director2', 1974, 'Country2', 'Ganre1'),
	(3, 'Director3', 1988, 'Country3', 'Ganre1'),
	(4, 'Director4', 1955, 'Country2', 'Ganre3'),
	(5, 'Director5', 1950, 'Country1', 'Ganre3');

CREATE TABLE IF NOT EXISTS `studios` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `creation_year` year(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

INSERT INTO `studios` (`id`, `name`, `country`, `creation_year`) VALUES
	(1, 'DC', 'Country1', 1990),
	(2, 'Studio2', 'Country2', 2000),
	(3, 'Studio3', 'Country2', 1985),
	(4, 'Marvel', 'USA', 1993);

CREATE TABLE IF NOT EXISTS `films` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `ganre` varchar(100) NOT NULL,
  `filmed_year` year(4) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `budget` int(10) NOT NULL,
  `studio_id` int(10) NOT NULL,
  `director_id` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `director_fk0` (`director_id`),
  KEY `films_fk1` (`studio_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

INSERT INTO `films` (`id`, `name`, `country`, `ganre`, `filmed_year`, `duration`, `budget`, `studio_id`, `director_id`) VALUES
	(1, 'Film1', 'Country1', 'Ganre2', 1999, '120 minutes', 200000, 2, 2),
	(4, 'Film2', 'Country2', 'Ganre3', 2000, '02:11:00', 100000, 1, 1),
	(5, 'Film3', 'USA', 'Ganre1', 1983, '00:45:50', 45000, 3, 4);

CREATE TABLE IF NOT EXISTS `production` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `film_id` int(10) NOT NULL,
  `actor_id` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `actor_fk0` (`actor_id`),
  KEY `production_fk1` (`film_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

INSERT INTO `production` (`id`, `film_id`, `actor_id`) VALUES
	(1, 1, 2),
	(2, 1, 1),
	(5, 4, 2);

ALTER TABLE `films`
  ADD CONSTRAINT `films_fk1` FOREIGN KEY (`studio_id`) REFERENCES `studios` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `films_ibfk_1` FOREIGN KEY (`director_id`) REFERENCES `directors` (`id`) ON DELETE CASCADE;

ALTER TABLE `production`
  ADD CONSTRAINT `production_fk1` FOREIGN KEY (`film_id`) REFERENCES `films` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `production_ibfk_1` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`) ON DELETE CASCADE;
