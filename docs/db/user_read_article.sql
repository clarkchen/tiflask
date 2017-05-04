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

 Date: 04/09/2017 21:55:49 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user_read_article`
-- ----------------------------
DROP TABLE IF EXISTS `user_read_article`;
CREATE TABLE `user_read_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL COMMENT '文章编号',
  `create_time` datetime DEFAULT NULL COMMENT '阅读时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `user_read_article`
-- ----------------------------
BEGIN;
INSERT INTO `user_read_article` VALUES ('1', '1', '1', '2016-02-01 23:17:47'), ('2', '1', '2', '2016-07-17 23:18:03');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
