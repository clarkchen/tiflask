/*
 Navicat Premium Data Transfer

 Source Server         : monitor
 Source Server Type    : MySQL
 Source Server Version : 50540
 Source Host           : 121.42.146.188
 Source Database       : demo

 Target Server Type    : MySQL
 Target Server Version : 50540
 File Encoding         : utf-8

 Date: 04/09/2017 21:55:42 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user_info`
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '用户姓名',
  `reg_date` datetime DEFAULT NULL COMMENT '注册日期',
  `phone` varchar(50) COLLATE utf8_bin DEFAULT NULL COMMENT '电话号码',
  `province` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_on_phone` (`phone`),
  KEY `index_on_time` (`reg_date`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `user_info`
-- ----------------------------
BEGIN;
INSERT INTO `user_info` VALUES ('1', 'clarkchen', '2016-07-17 23:03:35', '18500195632', '朝阳', '北京'), ('2', 'test', '2016-09-18 00:00:00', '123123', '北京', 'abc'), ('3', 'test', '2016-09-18 00:00:00', '123123', 'china', 'abc'), ('4', 'test', '2016-09-18 00:00:00', '123123', 'china', 'abc');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
