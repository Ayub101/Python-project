-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2021 at 01:06 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `skars shopping`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `log_id` varchar(30) NOT NULL,
  `feedback` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `log_id` varchar(30) NOT NULL,
  `pass_word` varchar(15) NOT NULL,
  `User_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`log_id`, `pass_word`, `User_name`) VALUES
('kayub4947@gmail.com', '123456789', 'Ayub Khan'),
('riyaztech@gmail.com', 'riyaz@1234', 'riyaz');

-- --------------------------------------------------------

--
-- Table structure for table `reminder_list`
--

CREATE TABLE `reminder_list` (
  `Wish_id` int(11) NOT NULL,
  `rem_time` varchar(11) NOT NULL,
  `rem_date` varchar(15) NOT NULL,
  `check_tm` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reminder_list`
--

INSERT INTO `reminder_list` (`Wish_id`, `rem_time`, `rem_date`, `check_tm`) VALUES
(2, '16:24', '2021-04-11', '3Hr'),
(3, '16:59', '2021-04-11', '3Hr');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `log_id` varchar(30) NOT NULL,
  `Product_name` varchar(150) NOT NULL,
  `review` varchar(300) NOT NULL,
  `star` int(5) NOT NULL,
  `date` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`log_id`, `Product_name`, `review`, `star`, `date`) VALUES
('kayub4947@gmail.com', 'Mi 10i Midnight Black 6GB+128GB', 'good product but price is so high\n', 3, '2021-04-11'),
('kayub4947@gmail.com', 'Mi 10i Pacific Sunrise 6GB+128GB', 'Best Product  of mi\n', 5, '2021-05-01'),
('kayub4947@gmail.com', 'Redmi 9 Power (4GB RAM, 64GB Storage, Blazing Blue)', 'yes riyaz , this is awesome product  \n', 5, '2021-04-11'),
('kayub4947@gmail.com', 'Redmi Note 10 Shadow Black 6GB+128GB', 'This product is very good it has a good and battery life is also good only problem is with its camera ', 4, '2021-04-11'),
('riyaztech@gmail.com', 'OPPO A53 4 GB 64 GB Electric Black', 'nice product and nice price\n', 5, '2021-04-11'),
('riyaztech@gmail.com', 'Redmi 9 Power (4GB RAM, 64GB Storage, Blazing Blue)', 'nice product\n', 5, '2021-04-11'),
('riyaztech@gmail.com', 'Redmi 9 Power Mighty Black 6GB+128GB', 'good product go and buy it\n', 4, '2021-04-11'),
('riyaztech@gmail.com', 'Redmi Note 10 Shadow Black 6GB+128GB', 'This product is so awesome go and buy it\n', 4, '2021-04-11');

-- --------------------------------------------------------

--
-- Table structure for table `wishlist`
--

CREATE TABLE `wishlist` (
  `Wish_id` int(5) NOT NULL,
  `log_id` varchar(30) NOT NULL,
  `Product_name` varchar(150) NOT NULL,
  `price` varchar(12) NOT NULL,
  `Store_name` varchar(30) NOT NULL,
  `link` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wishlist`
--

INSERT INTO `wishlist` (`Wish_id`, `log_id`, `Product_name`, `price`, `Store_name`, `link`) VALUES
(2, 'kayub4947@gmail.com', 'Redmi Note 10 Shadow Black 6GB+128GB', '₹13,999.00', ' from Mi.com', 'http://www.google.com/aclk?sa=L&ai=DChcSEwi72OXDm-rvAhVR10wCHUl8CPEYABBUGgJ0bQ&sig=AOD64_1r7umvu4ifW-Kdn4slFSo6a9pyaQ&ctype=5&ved=0ahUKEwimqd7Dm-rvAhUUeisKHSPdCTgQ2CkIlQI&adurl='),
(3, 'kayub4947@gmail.com', 'Redmi 9 Power (4GB RAM, 64GB Storage, Blazing Blue)', '₹10,499.00', ' from Flipkart', 'http://www.flipkart.com/redmi-9-power-blazing-blue-64-gb/p/itm9533b02ba34ef%3Fpid%3DMOBFYZ7HHGJUATYD%26lid%3DLSTMOBFYZ7HHGJUATYDFYZRIS%26marketplace%3DFLIPKART%26cmpid%3Dcontent_mobile_8965229628_gmc&'),
(4, 'kayub4947@gmail.com', 'Redmi 9 Power Mighty Black 6GB+128GB', '₹12,999.00', ' from Mi.com', 'http://www.google.com/aclk?sa=L&ai=DChcSEwi72OXDm-rvAhVR10wCHUl8CPEYABBVGgJ0bQ&sig=AOD64_3dGsII_G2Lm4XcNzBlEdEe_DWNEA&ctype=5&ved=0ahUKEwimqd7Dm-rvAhUUeisKHSPdCTgQ2CkInAI&adurl='),
(5, 'kayub4947@gmail.com', 'Redmi 9 Power Blazing Blue 6GB+128GB', '₹12,999.00', ' from Mi.com', 'http://www.google.com/aclk?sa=L&ai=DChcSEwi72OXDm-rvAhVR10wCHUl8CPEYABBWGgJ0bQ&sig=AOD64_3-gVOIdizhgCBh2yXXfzdFFfEJJQ&ctype=5&ved=0ahUKEwimqd7Dm-rvAhUUeisKHSPdCTgQ2CkInwI&adurl='),
(6, 'kayub4947@gmail.com', 'Mi 10i Midnight Black 8GB+128GB', '₹23,999.00', ' from Mi.com', 'http://www.google.com/aclk?sa=L&ai=DChcSEwi72OXDm-rvAhVR10wCHUl8CPEYABBXGgJ0bQ&sig=AOD64_2Jp3Ft5R337Vu8SguK2EgdfhPb5A&ctype=5&ved=0ahUKEwimqd7Dm-rvAhUUeisKHSPdCTgQ2CkIogI&adurl='),
(7, 'kayub4947@gmail.com', 'Xiaomi Mi 10i (Atlantic Blue, 64GB, 6GB RAM)', '₹20,500.00', ' from Gadgets Now', 'http://www.google.com/aclk?sa=L&ai=DChcSEwi72OXDm-rvAhVR10wCHUl8CPEYABBcGgJ0bQ&sig=AOD64_28XBVZbQfCUlT13zLHDK8R8vY_bg&ctype=5&ved=0ahUKEwimqd7Dm-rvAhUUeisKHSPdCTgQ2CkIpQI&adurl='),
(8, 'kayub4947@gmail.com', 'Redmi Note 10 Aqua Green 6GB+128GB', '₹13,999.00', ' from Mi.com', 'http://www.google.com/aclk?sa=L&ai=DChcSEwjzoIjCru7vAhUSBZEKHWzPB3AYABBUGgJjZQ&sig=AOD64_2oQbtqBgXbPWMMmxNQtbpgnSwndw&ctype=5&ved=0ahUKEwjC2oPCru7vAhWBK7kGHbP2B9EQ2CkIkgI&adurl=');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`log_id`);

--
-- Indexes for table `reminder_list`
--
ALTER TABLE `reminder_list`
  ADD PRIMARY KEY (`Wish_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`log_id`,`Product_name`);

--
-- Indexes for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD PRIMARY KEY (`Wish_id`),
  ADD KEY `log_id` (`log_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `wishlist`
--
ALTER TABLE `wishlist`
  MODIFY `Wish_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feedback`
--
ALTER TABLE `feedback`
  ADD CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`log_id`) REFERENCES `login` (`log_id`);

--
-- Constraints for table `reminder_list`
--
ALTER TABLE `reminder_list`
  ADD CONSTRAINT `reminder_list_ibfk_1` FOREIGN KEY (`Wish_id`) REFERENCES `wishlist` (`Wish_id`);

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`log_id`) REFERENCES `login` (`log_id`);

--
-- Constraints for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`log_id`) REFERENCES `login` (`log_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
