-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-12-2024 a las 22:35:02
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dungeon_and_dragons`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `armas`
--

CREATE TABLE `armas` (
  `ARM_id` int(11) NOT NULL,
  `ARM_nombre` varchar(45) NOT NULL,
  `ARM_danho` int(11) NOT NULL,
  `ARM_nivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `EQU_id` int(11) NOT NULL,
  `EQU_nombre` varchar(45) NOT NULL,
  `EQU_JUG_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escudos`
--

CREATE TABLE `escudos` (
  `ESC_id` int(11) NOT NULL,
  `ESC_nombre` varchar(45) NOT NULL,
  `ESC_defensa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventarios`
--

CREATE TABLE `inventarios` (
  `INV_id` int(11) NOT NULL,
  `INV_ARM_id` int(11) NOT NULL,
  `INV_ESC_id` int(11) NOT NULL,
  `INV_POC_id` int(11) NOT NULL,
  `INV_capacidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugadores`
--

CREATE TABLE `jugadores` (
  `JUG_id` int(11) NOT NULL,
  `JUG_nombre` varchar(45) NOT NULL,
  `JUG_nivel` int(11) NOT NULL,
  `JUG_salud` int(11) NOT NULL,
  `JUG_raza` varchar(45) NOT NULL,
  `JUG_experiencia` int(11) NOT NULL,
  `JUG_INV_id` int(11) NOT NULL,
  `JUG_puntaje` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pociones`
--

CREATE TABLE `pociones` (
  `POC_id` int(11) NOT NULL,
  `POC_nombre` varchar(45) NOT NULL,
  `POC_cura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ranking`
--

CREATE TABLE `ranking` (
  `RG_id` int(11) NOT NULL,
  `RG_puntaje` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ranking`
--

INSERT INTO `ranking` (`RG_id`, `RG_puntaje`) VALUES
(1, 1),
(2, 0),
(3, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `USU_id` int(11) NOT NULL,
  `USU_nombre` varchar(45) NOT NULL,
  `USU_pass` varchar(150) NOT NULL,
  `USU_correo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`USU_id`, `USU_nombre`, `USU_pass`, `USU_correo`) VALUES
(2, 'Giovanni', '$2b$12$t.irGGZeKXTnKYFZSeUFj.25KMTLzq8rA.3uJk', 'giodirosa@gmail.cl'),
(3, 'dino', '$2b$12$VsfQaiWJ6kzHnuBkaD1sseLiDUNBXz1EFNweM2', 'dino@correo.cl'),
(4, 'dante', '$2b$12$gt51pmrofxcAkOVJtZ.b/OcJyJYhp6Wu8f0o7r', 'dante@gmail.cl'),
(5, 'sofia', '$argon2id$v=19$m=65536,t=3,p=4$MjUgg98H2xntAj', 'sofia@gmail.cl'),
(6, 'prueba', '$argon2id$v=19$m=65536,t=3,p=4$BPJ/0H2h/TPD3K', 'prueba@correo.cl'),
(7, 'danilo', '$argon2id$v=19$m=65536,t=3,p=4$wO1v//0x5ikyqM', 'danilo@correo.cl'),
(8, 'libertad', '$argon2id$v=19$m=65536,t=3,p=4$ChsFIacEg/fNd1', 'libertad@gmail.cl'),
(9, 'demo', '$argon2id$v=19$m=65536,t=3,p=4$9cLGnal9amznwtl73cR14w$YVvo2TvLdrfhb6aELNlTnTplCujniv72kAmRB5aLQXQ', 'demo@correo.cl'),
(10, 'demo', '$argon2id$v=19$m=65536,t=3,p=4$KkmBKBkgGTpfPGIS85z3hg$kL3jNDWHus62ic9TqOoo2wdweENpC7Ewc4n+pneDMoE', 'demo12@correo.cl'),
(11, 'demo24', '$argon2id$v=19$m=65536,t=3,p=4$FdfdBOrH+D/EM7EwxXmhvA$9KMIVRVMmIoRkJ9JqV8ONLR+W3O/Xu0RwUhq7inDN9Q', 'demo24@correo.cl'),
(12, 'nicolas', '$argon2id$v=19$m=65536,t=3,p=4$5sO/+BF9Cs9vnHtCj+Db2A$IbPz8C3ICZWfqO4RfoicMiutYMrREeBdRDg7jj+UxRY', 'nicolas@correo.cl'),
(13, 'gio3', '$argon2id$v=19$m=65536,t=3,p=4$9wt/nIip/7hAXbAaTFaKeA$lOCPetvPRFeNrs4tsW39IbFlHlcHocTMW3aw+madv8s', 'gio@correo.cl'),
(14, 'adi', '$argon2id$v=19$m=65536,t=3,p=4$wiE/Lsbr54RqKz2+f3KoOQ$mBbyhJ3Ir93U8ubSo4TSIyG3AVk9eKaWpkLyR3hXR8Q', 'adi@corre.cl'),
(15, 'giodirosa', '$argon2id$v=19$m=65536,t=3,p=4$pK4Dr82/SYiUXouHDD25rA$ObmXe3DcLWGo8K3oOuGRdJum7FaqGWnbCuZ+DAvEXM4', 'gio@correo.cl'),
(16, 'matiasmora', '$argon2id$v=19$m=65536,t=3,p=4$C1BTVW2O69d2lcJdPoBx+A$f6c5uxaEvgL58BrZk5jCvy5VA6NYPD+gGZ195CdlGEY', 'matias@correo.cl'),
(17, 'nico', '$argon2id$v=19$m=65536,t=3,p=4$Ve0Vrqj9KSw6UcRHVyCNww$RFR/nfDuHG8BIqKuDPFLv6FnJn4LFFpFhhWDrh4HnzU', 'nico@correo.cl'),
(18, 'luis', '$argon2id$v=19$m=65536,t=3,p=4$lRbkR+peP0M0il6e/NGFZw$wz10OzaJ5kpeo7xItgMOx09NWkeGQpZsC5RPzdgI554', 'luis@correo.cl'),
(19, 'ra', '$argon2id$v=19$m=65536,t=3,p=4$F+X5JHFE2eqjeGSHFu/EXQ$xZJbKC6w474RyvP49VgrUYcQvv1hqf77FSPYvkieO1M', 'ra@correo.cl'),
(20, 'matti', '$argon2id$v=19$m=65536,t=3,p=4$uCJQeACtfYtmJ60wmO/hgA$cNbCaCOTk73PIDrEHWNXRTHsjghEqLk30DyPaxPSpNI', 'matti@correo.cl');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `armas`
--
ALTER TABLE `armas`
  ADD PRIMARY KEY (`ARM_id`);

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`EQU_id`),
  ADD KEY `fk_EQU_JUG` (`EQU_JUG_id`);

--
-- Indices de la tabla `escudos`
--
ALTER TABLE `escudos`
  ADD PRIMARY KEY (`ESC_id`);

--
-- Indices de la tabla `inventarios`
--
ALTER TABLE `inventarios`
  ADD PRIMARY KEY (`INV_id`),
  ADD KEY `fk_INV_ARM` (`INV_ARM_id`),
  ADD KEY `fk_INV_ESC` (`INV_ESC_id`),
  ADD KEY `fk_INV_POC` (`INV_POC_id`);

--
-- Indices de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`JUG_id`),
  ADD KEY `fk_JUG_INV` (`JUG_INV_id`);

--
-- Indices de la tabla `pociones`
--
ALTER TABLE `pociones`
  ADD PRIMARY KEY (`POC_id`);

--
-- Indices de la tabla `ranking`
--
ALTER TABLE `ranking`
  ADD PRIMARY KEY (`RG_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`USU_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `armas`
--
ALTER TABLE `armas`
  MODIFY `ARM_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `EQU_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escudos`
--
ALTER TABLE `escudos`
  MODIFY `ESC_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventarios`
--
ALTER TABLE `inventarios`
  MODIFY `INV_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  MODIFY `JUG_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pociones`
--
ALTER TABLE `pociones`
  MODIFY `POC_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ranking`
--
ALTER TABLE `ranking`
  MODIFY `RG_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `USU_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD CONSTRAINT `fk_EQU_JUG` FOREIGN KEY (`EQU_JUG_id`) REFERENCES `jugadores` (`JUG_id`);

--
-- Filtros para la tabla `inventarios`
--
ALTER TABLE `inventarios`
  ADD CONSTRAINT `fk_INV_ARM` FOREIGN KEY (`INV_ARM_id`) REFERENCES `armas` (`ARM_id`),
  ADD CONSTRAINT `fk_INV_ESC` FOREIGN KEY (`INV_ESC_id`) REFERENCES `escudos` (`ESC_id`),
  ADD CONSTRAINT `fk_INV_POC` FOREIGN KEY (`INV_POC_id`) REFERENCES `pociones` (`POC_id`);

--
-- Filtros para la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD CONSTRAINT `fk_JUG_INV` FOREIGN KEY (`JUG_INV_id`) REFERENCES `inventarios` (`INV_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
