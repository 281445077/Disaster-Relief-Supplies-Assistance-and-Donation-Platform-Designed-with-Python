/*
Navicat MySQL Data Transfer

Source Server         : localhost_3308
Source Server Version : 80012
Source Host           : localhost:3308
Source Database       : pythons12288jypythondzzwzqzyjzptsjysx

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2022-04-10 17:15:23
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `admins`
-- ----------------------------
DROP TABLE IF EXISTS `admins`;
CREATE TABLE `admins` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pwd` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of admins
-- ----------------------------
INSERT INTO `admins` VALUES ('1', 'admin', 'admin');

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=109 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add 管理员', '1', 'add_admins');
INSERT INTO `auth_permission` VALUES ('2', 'Can change 管理员', '1', 'change_admins');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete 管理员', '1', 'delete_admins');
INSERT INTO `auth_permission` VALUES ('4', 'Can view 管理员', '1', 'view_admins');
INSERT INTO `auth_permission` VALUES ('5', 'Can add 新闻分类', '2', 'add_xinwenfenlei');
INSERT INTO `auth_permission` VALUES ('6', 'Can change 新闻分类', '2', 'change_xinwenfenlei');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete 新闻分类', '2', 'delete_xinwenfenlei');
INSERT INTO `auth_permission` VALUES ('8', 'Can view 新闻分类', '2', 'view_xinwenfenlei');
INSERT INTO `auth_permission` VALUES ('9', 'Can add 新闻信息', '3', 'add_xinwenxinxi');
INSERT INTO `auth_permission` VALUES ('10', 'Can change 新闻信息', '3', 'change_xinwenxinxi');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete 新闻信息', '3', 'delete_xinwenxinxi');
INSERT INTO `auth_permission` VALUES ('12', 'Can view 新闻信息', '3', 'view_xinwenxinxi');
INSERT INTO `auth_permission` VALUES ('13', 'Can add 友情链接', '4', 'add_youqinglianjie');
INSERT INTO `auth_permission` VALUES ('14', 'Can change 友情链接', '4', 'change_youqinglianjie');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete 友情链接', '4', 'delete_youqinglianjie');
INSERT INTO `auth_permission` VALUES ('16', 'Can view 友情链接', '4', 'view_youqinglianjie');
INSERT INTO `auth_permission` VALUES ('17', 'Can add 留言信息', '5', 'add_liuyanxinxi');
INSERT INTO `auth_permission` VALUES ('18', 'Can change 留言信息', '5', 'change_liuyanxinxi');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete 留言信息', '5', 'delete_liuyanxinxi');
INSERT INTO `auth_permission` VALUES ('20', 'Can view 留言信息', '5', 'view_liuyanxinxi');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 轮播图', '6', 'add_lunbotu');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 轮播图', '6', 'change_lunbotu');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 轮播图', '6', 'delete_lunbotu');
INSERT INTO `auth_permission` VALUES ('24', 'Can view 轮播图', '6', 'view_lunbotu');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 用户', '7', 'add_yonghu');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 用户', '7', 'change_yonghu');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 用户', '7', 'delete_yonghu');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 用户', '7', 'view_yonghu');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 捐赠', '8', 'add_juanzeng');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 捐赠', '8', 'change_juanzeng');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 捐赠', '8', 'delete_juanzeng');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 捐赠', '8', 'view_juanzeng');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 捐赠审核', '9', 'add_juanzengshenhe');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 捐赠审核', '9', 'change_juanzengshenhe');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 捐赠审核', '9', 'delete_juanzengshenhe');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 捐赠审核', '9', 'view_juanzengshenhe');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 捐寄', '10', 'add_juanji');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 捐寄', '10', 'change_juanji');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 捐寄', '10', 'delete_juanji');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 捐寄', '10', 'view_juanji');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 捐寄审核', '11', 'add_juanjishenhe');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 捐寄审核', '11', 'change_juanjishenhe');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 捐寄审核', '11', 'delete_juanjishenhe');
INSERT INTO `auth_permission` VALUES ('44', 'Can view 捐寄审核', '11', 'view_juanjishenhe');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 处理', '12', 'add_chuli');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 处理', '12', 'change_chuli');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 处理', '12', 'delete_chuli');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 处理', '12', 'view_chuli');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 需求信息', '13', 'add_xuqiuxinxi');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 需求信息', '13', 'change_xuqiuxinxi');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 需求信息', '13', 'delete_xuqiuxinxi');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 需求信息', '13', 'view_xuqiuxinxi');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 需求审核', '14', 'add_xuqiushenhe');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 需求审核', '14', 'change_xuqiushenhe');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 需求审核', '14', 'delete_xuqiushenhe');
INSERT INTO `auth_permission` VALUES ('56', 'Can view 需求审核', '14', 'view_xuqiushenhe');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 捐赠物资', '15', 'add_juanzengwuzi');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 捐赠物资', '15', 'change_juanzengwuzi');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 捐赠物资', '15', 'delete_juanzengwuzi');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 捐赠物资', '15', 'view_juanzengwuzi');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 领取', '16', 'add_lingqu');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 领取', '16', 'change_lingqu');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 领取', '16', 'delete_lingqu');
INSERT INTO `auth_permission` VALUES ('64', 'Can view 领取', '16', 'view_lingqu');
INSERT INTO `auth_permission` VALUES ('65', 'Can add 申领', '17', 'add_shenling');
INSERT INTO `auth_permission` VALUES ('66', 'Can change 申领', '17', 'change_shenling');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete 申领', '17', 'delete_shenling');
INSERT INTO `auth_permission` VALUES ('68', 'Can view 申领', '17', 'view_shenling');
INSERT INTO `auth_permission` VALUES ('69', 'Can add 申领审核', '18', 'add_shenlingshenhe');
INSERT INTO `auth_permission` VALUES ('70', 'Can change 申领审核', '18', 'change_shenlingshenhe');
INSERT INTO `auth_permission` VALUES ('71', 'Can delete 申领审核', '18', 'delete_shenlingshenhe');
INSERT INTO `auth_permission` VALUES ('72', 'Can view 申领审核', '18', 'view_shenlingshenhe');
INSERT INTO `auth_permission` VALUES ('73', 'Can add 派寄', '19', 'add_paiji');
INSERT INTO `auth_permission` VALUES ('74', 'Can change 派寄', '19', 'change_paiji');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete 派寄', '19', 'delete_paiji');
INSERT INTO `auth_permission` VALUES ('76', 'Can view 派寄', '19', 'view_paiji');
INSERT INTO `auth_permission` VALUES ('77', 'Can add 签收', '20', 'add_qianshou');
INSERT INTO `auth_permission` VALUES ('78', 'Can change 签收', '20', 'change_qianshou');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete 签收', '20', 'delete_qianshou');
INSERT INTO `auth_permission` VALUES ('80', 'Can view 签收', '20', 'view_qianshou');
INSERT INTO `auth_permission` VALUES ('81', 'Can add 物品类别', '21', 'add_wupinleibie');
INSERT INTO `auth_permission` VALUES ('82', 'Can change 物品类别', '21', 'change_wupinleibie');
INSERT INTO `auth_permission` VALUES ('83', 'Can delete 物品类别', '21', 'delete_wupinleibie');
INSERT INTO `auth_permission` VALUES ('84', 'Can view 物品类别', '21', 'view_wupinleibie');
INSERT INTO `auth_permission` VALUES ('85', 'Can add log entry', '22', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('86', 'Can change log entry', '22', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('87', 'Can delete log entry', '22', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('88', 'Can view log entry', '22', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('89', 'Can add permission', '23', 'add_permission');
INSERT INTO `auth_permission` VALUES ('90', 'Can change permission', '23', 'change_permission');
INSERT INTO `auth_permission` VALUES ('91', 'Can delete permission', '23', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('92', 'Can view permission', '23', 'view_permission');
INSERT INTO `auth_permission` VALUES ('93', 'Can add group', '24', 'add_group');
INSERT INTO `auth_permission` VALUES ('94', 'Can change group', '24', 'change_group');
INSERT INTO `auth_permission` VALUES ('95', 'Can delete group', '24', 'delete_group');
INSERT INTO `auth_permission` VALUES ('96', 'Can view group', '24', 'view_group');
INSERT INTO `auth_permission` VALUES ('97', 'Can add user', '25', 'add_user');
INSERT INTO `auth_permission` VALUES ('98', 'Can change user', '25', 'change_user');
INSERT INTO `auth_permission` VALUES ('99', 'Can delete user', '25', 'delete_user');
INSERT INTO `auth_permission` VALUES ('100', 'Can view user', '25', 'view_user');
INSERT INTO `auth_permission` VALUES ('101', 'Can add content type', '26', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('102', 'Can change content type', '26', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('103', 'Can delete content type', '26', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('104', 'Can view content type', '26', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('105', 'Can add session', '27', 'add_session');
INSERT INTO `auth_permission` VALUES ('106', 'Can change session', '27', 'change_session');
INSERT INTO `auth_permission` VALUES ('107', 'Can delete session', '27', 'delete_session');
INSERT INTO `auth_permission` VALUES ('108', 'Can view session', '27', 'view_session');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `chuli`
-- ----------------------------
DROP TABLE IF EXISTS `chuli`;
CREATE TABLE `chuli` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `leixing` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `beizhuxinxi` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tianjiaren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanjiid` bigint(20) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chuli_juanjiid_e5bd380b` (`juanjiid`),
  KEY `chuli_juanzengid_170af70e` (`juanzengid`),
  KEY `chuli_wupinleibie_4d259998` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of chuli
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admins', 'admins');
INSERT INTO `django_content_type` VALUES ('2', 'xinwenfenlei', 'xinwenfenlei');
INSERT INTO `django_content_type` VALUES ('3', 'xinwenxinxi', 'xinwenxinxi');
INSERT INTO `django_content_type` VALUES ('4', 'youqinglianjie', 'youqinglianjie');
INSERT INTO `django_content_type` VALUES ('5', 'liuyanxinxi', 'liuyanxinxi');
INSERT INTO `django_content_type` VALUES ('6', 'lunbotu', 'lunbotu');
INSERT INTO `django_content_type` VALUES ('7', 'yonghu', 'yonghu');
INSERT INTO `django_content_type` VALUES ('8', 'juanzeng', 'juanzeng');
INSERT INTO `django_content_type` VALUES ('9', 'juanzengshenhe', 'juanzengshenhe');
INSERT INTO `django_content_type` VALUES ('10', 'juanji', 'juanji');
INSERT INTO `django_content_type` VALUES ('11', 'juanjishenhe', 'juanjishenhe');
INSERT INTO `django_content_type` VALUES ('12', 'chuli', 'chuli');
INSERT INTO `django_content_type` VALUES ('13', 'xuqiuxinxi', 'xuqiuxinxi');
INSERT INTO `django_content_type` VALUES ('14', 'xuqiushenhe', 'xuqiushenhe');
INSERT INTO `django_content_type` VALUES ('15', 'juanzengwuzi', 'juanzengwuzi');
INSERT INTO `django_content_type` VALUES ('16', 'lingqu', 'lingqu');
INSERT INTO `django_content_type` VALUES ('17', 'shenling', 'shenling');
INSERT INTO `django_content_type` VALUES ('18', 'shenlingshenhe', 'shenlingshenhe');
INSERT INTO `django_content_type` VALUES ('19', 'paiji', 'paiji');
INSERT INTO `django_content_type` VALUES ('20', 'qianshou', 'qianshou');
INSERT INTO `django_content_type` VALUES ('21', 'wupinleibie', 'wupinleibie');
INSERT INTO `django_content_type` VALUES ('22', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('23', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('24', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('25', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('26', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('27', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2022-04-10 14:43:38.129995');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2022-04-10 14:43:39.372572');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2022-04-10 14:43:39.633318');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2022-04-10 14:43:39.639861');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2022-04-10 14:43:39.644688');
INSERT INTO `django_migrations` VALUES ('6', 'admins', '0001_initial', '2022-04-10 14:43:39.667555');
INSERT INTO `django_migrations` VALUES ('7', 'contenttypes', '0002_remove_content_type_name', '2022-04-10 14:43:39.796562');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2022-04-10 14:43:39.869435');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2022-04-10 14:43:39.932239');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2022-04-10 14:43:39.937225');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2022-04-10 14:43:39.993077');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2022-04-10 14:43:39.995071');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2022-04-10 14:43:40.003050');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2022-04-10 14:43:40.084830');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0009_alter_user_last_name_max_length', '2022-04-10 14:43:40.148659');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0010_alter_group_name_max_length', '2022-04-10 14:43:40.211491');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0011_update_proxy_permissions', '2022-04-10 14:43:40.218473');
INSERT INTO `django_migrations` VALUES ('18', 'auth', '0012_alter_user_first_name_max_length', '2022-04-10 14:43:40.292706');
INSERT INTO `django_migrations` VALUES ('19', 'wupinleibie', '0001_initial', '2022-04-10 14:43:40.306632');
INSERT INTO `django_migrations` VALUES ('20', 'juanzeng', '0001_initial', '2022-04-10 14:43:40.446715');
INSERT INTO `django_migrations` VALUES ('21', 'juanji', '0001_initial', '2022-04-10 14:43:40.721254');
INSERT INTO `django_migrations` VALUES ('22', 'chuli', '0001_initial', '2022-04-10 14:43:41.137330');
INSERT INTO `django_migrations` VALUES ('23', 'juanjishenhe', '0001_initial', '2022-04-10 14:43:41.546485');
INSERT INTO `django_migrations` VALUES ('24', 'juanzengshenhe', '0001_initial', '2022-04-10 14:43:41.712439');
INSERT INTO `django_migrations` VALUES ('25', 'xuqiuxinxi', '0001_initial', '2022-04-10 14:43:41.797210');
INSERT INTO `django_migrations` VALUES ('26', 'juanzengwuzi', '0001_initial', '2022-04-10 14:43:41.998716');
INSERT INTO `django_migrations` VALUES ('27', 'lingqu', '0001_initial', '2022-04-10 14:43:42.139281');
INSERT INTO `django_migrations` VALUES ('28', 'liuyanxinxi', '0001_initial', '2022-04-10 14:43:42.153243');
INSERT INTO `django_migrations` VALUES ('29', 'lunbotu', '0001_initial', '2022-04-10 14:43:42.167206');
INSERT INTO `django_migrations` VALUES ('30', 'shenling', '0001_initial', '2022-04-10 14:43:42.324108');
INSERT INTO `django_migrations` VALUES ('31', 'paiji', '0001_initial', '2022-04-10 14:43:42.552620');
INSERT INTO `django_migrations` VALUES ('32', 'qianshou', '0001_initial', '2022-04-10 14:43:43.091483');
INSERT INTO `django_migrations` VALUES ('33', 'sessions', '0001_initial', '2022-04-10 14:43:43.177670');
INSERT INTO `django_migrations` VALUES ('34', 'shenlingshenhe', '0001_initial', '2022-04-10 14:43:43.634984');
INSERT INTO `django_migrations` VALUES ('35', 'xinwenfenlei', '0001_initial', '2022-04-10 14:43:43.645957');
INSERT INTO `django_migrations` VALUES ('36', 'xinwenxinxi', '0001_initial', '2022-04-10 14:43:43.755661');
INSERT INTO `django_migrations` VALUES ('37', 'xuqiushenhe', '0001_initial', '2022-04-10 14:43:43.907591');
INSERT INTO `django_migrations` VALUES ('38', 'yonghu', '0001_initial', '2022-04-10 14:43:43.924407');
INSERT INTO `django_migrations` VALUES ('39', 'youqinglianjie', '0001_initial', '2022-04-10 14:43:43.934610');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('ol4fd5f27ndxwpoxaz9nau4cgm5h1nug', '.eJyrVkpOLChJzkh0zk9JVbJSMrYwNFHSUUquALJjSs2TEg2BpImBWUypqYmpBVAmJz89Mw-XZGlxalFeYi7IoMSUXKA6HaXMFCDHEMgoKE-BC9cCACdUIrk:1ndTOV:ogFFhB3g1jj8cOLK_sSce9EZqP50dB060cjGOhf86d0', '2022-04-24 16:58:03.948331');

-- ----------------------------
-- Table structure for `juanji`
-- ----------------------------
DROP TABLE IF EXISTS `juanji`;
CREATE TABLE `juanji` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `wuliugongsi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `wuliudanhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `beizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `juanjizhuangtai` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `juanji_juanzengid_82e64558` (`juanzengid`),
  KEY `juanji_wupinleibie_18b81d82` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of juanji
-- ----------------------------
INSERT INTO `juanji` VALUES ('1', '16495747141090', '用品捐赠用品捐赠', '用品捐赠', '2', '001', '顺丰', 'sf45454545454', '', '未通过', '2022-04-10 15:24:28.908955', '6', '3');
INSERT INTO `juanji` VALUES ('2', '16495746638230', '食物捐赠食物捐赠', '食物', '2', '001', '顺丰', 'sf45454545451', '', '已通过', '2022-04-10 15:26:27.058055', '5', '2');
INSERT INTO `juanji` VALUES ('3', '16495745722810', '食物捐赠食物捐赠', '食物', '2', '001', '顺丰', 'sf45454545452', '', '已通过', '2022-04-10 15:26:32.662980', '4', '2');
INSERT INTO `juanji` VALUES ('4', '16495745472810', '衣服捐赠衣服捐赠', '衣服', '2', '001', '顺丰', 'sf454545454514', '', '已通过', '2022-04-10 15:26:39.396101', '3', '1');
INSERT INTO `juanji` VALUES ('5', '16495745083860', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '顺丰', 'sf454545454512', '', '已通过', '2022-04-10 15:26:48.325296', '2', '1');
INSERT INTO `juanji` VALUES ('6', '16495744484090', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '顺丰', 'sf45454545414', '', '已通过', '2022-04-10 15:26:54.418092', '1', '1');
INSERT INTO `juanji` VALUES ('7', '16495789098181', '衣物捐赠', '衣物', '2', '003', '顺丰', 'sf4545454545432', '', '已通过', '2022-04-10 16:23:29.087759', '7', '1');

-- ----------------------------
-- Table structure for `juanjishenhe`
-- ----------------------------
DROP TABLE IF EXISTS `juanjishenhe`;
CREATE TABLE `juanjishenhe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenhejieguo` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenhebeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `shenheren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanjiid` bigint(20) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `juanjishenhe_juanjiid_4936b9cc` (`juanjiid`),
  KEY `juanjishenhe_juanzengid_4486bad0` (`juanzengid`),
  KEY `juanjishenhe_wupinleibie_1858fd32` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of juanjishenhe
-- ----------------------------
INSERT INTO `juanjishenhe` VALUES ('1', '16495744484090', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:27:25.773162', '6', '1', '1');
INSERT INTO `juanjishenhe` VALUES ('2', '16495745083860', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:27:36.513449', '5', '2', '1');
INSERT INTO `juanjishenhe` VALUES ('3', '16495745472810', '衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:27:39.421238', '4', '3', '1');
INSERT INTO `juanjishenhe` VALUES ('4', '16495745722810', '食物捐赠食物捐赠', '食物', '2', '001', '已通过', '', 'admin', '2022-04-10 15:27:42.286035', '3', '4', '2');
INSERT INTO `juanjishenhe` VALUES ('5', '16495746638230', '食物捐赠食物捐赠', '食物', '2', '001', '已通过', '', 'admin', '2022-04-10 15:27:45.067736', '2', '5', '2');
INSERT INTO `juanjishenhe` VALUES ('6', '16495747141090', '用品捐赠用品捐赠', '用品捐赠', '2', '001', '未通过', '', 'admin', '2022-04-10 15:27:48.747237', '1', '6', '3');
INSERT INTO `juanjishenhe` VALUES ('7', '16495789098181', '衣物捐赠', '衣物', '2', '003', '已通过', '', 'admin', '2022-04-10 16:23:55.771766', '7', '7', '1');

-- ----------------------------
-- Table structure for `juanzeng`
-- ----------------------------
DROP TABLE IF EXISTS `juanzeng`;
CREATE TABLE `juanzeng` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tupian` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `xiangqingbeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `zhuangtai` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `juanzeng_wupinleibie_c6c61791` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of juanzeng
-- ----------------------------
INSERT INTO `juanzeng` VALUES ('1', '16495744484090', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '/upload/9483549249155681bb7d25896be015796506.png', '2', '<p>衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠</p>', '未被领取', '001', '2022-04-10 15:08:27.488879', '1');
INSERT INTO `juanzeng` VALUES ('2', '16495745083860', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '/upload/2f5ebcd01ecf5e189b037b9d31b556487442.png', '2', '<p><img src=\"https://img2.baidu.com/it/u=1703125137,1362261699&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=281\"/></p><p>衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠</p>', '未被领取', '001', '2022-04-10 15:09:02.865351', '1');
INSERT INTO `juanzeng` VALUES ('3', '16495745472810', '衣服捐赠衣服捐赠', '衣服', '/upload/6f34e239817c59d49dca4549c89249383512.png', '2', '<p>衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠衣服捐赠</p>', '未被领取', '001', '2022-04-10 15:09:31.449142', '1');
INSERT INTO `juanzeng` VALUES ('4', '16495745722810', '食物捐赠食物捐赠', '食物', '/upload/55ec11bff9fd5d4bb405893b46c1a5077233.png', '2', '<p>食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠</p>', '未被领取', '001', '2022-04-10 15:10:56.989405', '2');
INSERT INTO `juanzeng` VALUES ('5', '16495746638230', '食物捐赠食物捐赠', '食物', '/upload/065eb7d2c3d15a35afa24a2c4ce105975862.png', '2', '<p>食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠食物捐赠</p>', '未被领取', '001', '2022-04-10 15:11:33.051621', '2');
INSERT INTO `juanzeng` VALUES ('6', '16495747141090', '用品捐赠用品捐赠', '用品捐赠', '/upload/66befcb68a105d14a57f038de75127456621.png', '2', '<p>用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠用品捐赠</p>', '已处理', '001', '2022-04-10 15:12:22.394401', '3');
INSERT INTO `juanzeng` VALUES ('7', '16495789098181', '衣物捐赠', '衣物', '/upload/cffdd57e92a25a40ac165bb7e140b4952549.png,/upload/d3cbfd2d562258bd9bba72feee74e37b5579.png', '2', '<p>衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠衣物捐赠</p>', '已领取', '003', '2022-04-10 16:22:33.549726', '1');

-- ----------------------------
-- Table structure for `juanzengshenhe`
-- ----------------------------
DROP TABLE IF EXISTS `juanzengshenhe`;
CREATE TABLE `juanzengshenhe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenhejieguo` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenhebeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `shenheren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `juanzengshenhe_juanzengid_cdd206ef` (`juanzengid`),
  KEY `juanzengshenhe_wupinleibie_f5012d75` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of juanzengshenhe
-- ----------------------------
INSERT INTO `juanzengshenhe` VALUES ('1', '16495747141090', '用品捐赠用品捐赠', '用品捐赠', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:14.954448', '6', '3');
INSERT INTO `juanzengshenhe` VALUES ('2', '16495746638230', '食物捐赠食物捐赠', '食物', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:17.996655', '5', '2');
INSERT INTO `juanzengshenhe` VALUES ('3', '16495745472810', '衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:20.566638', '3', '1');
INSERT INTO `juanzengshenhe` VALUES ('4', '16495745722810', '食物捐赠食物捐赠', '食物', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:23.476337', '4', '2');
INSERT INTO `juanzengshenhe` VALUES ('5', '16495745083860', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:26.160074', '2', '1');
INSERT INTO `juanzengshenhe` VALUES ('6', '16495744484090', '衣服捐赠衣服捐赠衣服捐赠', '衣服', '2', '001', '已通过', '', 'admin', '2022-04-10 15:23:28.766815', '1', '1');
INSERT INTO `juanzengshenhe` VALUES ('7', '16495789098181', '衣物捐赠', '衣物', '2', '003', '已通过', '', 'admin', '2022-04-10 16:22:58.733669', '7', '1');

-- ----------------------------
-- Table structure for `juanzengwuzi`
-- ----------------------------
DROP TABLE IF EXISTS `juanzengwuzi`;
CREATE TABLE `juanzengwuzi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `xuqiubianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wuzhimingcheng` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `xingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shoujihao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `lianxidizhi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dengjiren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengwuzhi` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengshuliang` int(11) NOT NULL,
  `kuaidigongsi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `kuaididanhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengbeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `juanzengrennicheng` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengzhuangtai` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `wuzhileibie` bigint(20) NOT NULL,
  `xuqiuxinxiid` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `juanzengwuzi_wuzhileibie_2ab3ba46` (`wuzhileibie`),
  KEY `juanzengwuzi_xuqiuxinxiid_2ab497b0` (`xuqiuxinxiid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of juanzengwuzi
-- ----------------------------
INSERT INTO `juanzengwuzi` VALUES ('1', '16495805340393', '食物需求食物需求', '食物需求', '10', '小红', '12345678911', 'XXXX省XXX市XXX路', '004', '罐头', '10', '顺丰', 'sf123456', '', '小红', '已领取', '003', '2022-04-10 16:51:34.245567', '2', '4');

-- ----------------------------
-- Table structure for `lingqu`
-- ----------------------------
DROP TABLE IF EXISTS `lingqu`;
CREATE TABLE `lingqu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `xuqiubianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengwuzhi` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `juanzengshuliang` int(11) NOT NULL,
  `juanzengyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dengjiren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `lingqubeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengwuziid` bigint(20) NOT NULL,
  `xuqiuxinxiid` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lingqu_juanzengwuziid_30bac074` (`juanzengwuziid`),
  KEY `lingqu_xuqiuxinxiid_a340444a` (`xuqiuxinxiid`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of lingqu
-- ----------------------------
INSERT INTO `lingqu` VALUES ('1', '16495805340393', '食物需求食物需求', '罐头', '10', '003', '004', '', '2022-04-10 16:52:13.920090', '1', '4');

-- ----------------------------
-- Table structure for `liuyanxinxi`
-- ----------------------------
DROP TABLE IF EXISTS `liuyanxinxi`;
CREATE TABLE `liuyanxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `shouxinren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `xinxineirong` longtext COLLATE utf8_unicode_ci NOT NULL,
  `faxinren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `huifuneirong` longtext COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of liuyanxinxi
-- ----------------------------
INSERT INTO `liuyanxinxi` VALUES ('1', '004', '罐头要不要？', '003', '要，谢谢', '2022-04-10 16:50:27.647805');

-- ----------------------------
-- Table structure for `lunbotu`
-- ----------------------------
DROP TABLE IF EXISTS `lunbotu`;
CREATE TABLE `lunbotu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of lunbotu
-- ----------------------------
INSERT INTO `lunbotu` VALUES ('2', '2', '/upload/78bc27044d265d7e81cf9517ef732ffa8345.jpg', '#');
INSERT INTO `lunbotu` VALUES ('3', '2', '/upload/c7dacf3dfea75f2394500b261e9c9c5e7397.jpg', '#');

-- ----------------------------
-- Table structure for `paiji`
-- ----------------------------
DROP TABLE IF EXISTS `paiji`;
CREATE TABLE `paiji` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingbie` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrendianhua` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrendizhi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenqingyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `wuliugongsi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `wuliudanhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `beizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `caozuoren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `shenlingid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `paiji_juanzengid_4e2b99e9` (`juanzengid`),
  KEY `paiji_shenlingid_370fe050` (`shenlingid`),
  KEY `paiji_wupinleibie_e0bc4850` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of paiji
-- ----------------------------
INSERT INTO `paiji` VALUES ('1', '16495789098181', '衣物捐赠', '衣物', '2', '003', '赵三多', '男', '13612341234', 'XXX省XXX市XXX路', '004', '顺丰', 'sf4545454545432', '', 'admin', '2022-04-10 16:29:15.250130', '7', '1', '1');

-- ----------------------------
-- Table structure for `qianshou`
-- ----------------------------
DROP TABLE IF EXISTS `qianshou`;
CREATE TABLE `qianshou` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenqingyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `qianshoubeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `paijiid` bigint(20) NOT NULL,
  `shenlingid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qianshou_juanzengid_ac27d711` (`juanzengid`),
  KEY `qianshou_paijiid_32f30e60` (`paijiid`),
  KEY `qianshou_shenlingid_418d7541` (`shenlingid`),
  KEY `qianshou_wupinleibie_1856f1b2` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of qianshou
-- ----------------------------
INSERT INTO `qianshou` VALUES ('1', '16495789098181', '衣物捐赠', '衣物', '2', '003', '赵三多', '004', '', '2022-04-10 16:44:44.441866', '7', '1', '1', '1');

-- ----------------------------
-- Table structure for `shenling`
-- ----------------------------
DROP TABLE IF EXISTS `shenling`;
CREATE TABLE `shenling` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingbie` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrendianhua` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrendizhi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenqingmiaoshu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `shenlingzhuangtai` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenqingyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shenling_juanzengid_550ec7d5` (`juanzengid`),
  KEY `shenling_wupinleibie_f2023339` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of shenling
-- ----------------------------
INSERT INTO `shenling` VALUES ('1', '16495789098181', '衣物捐赠', '衣物', '2', '003', '赵三多', '男', '13612341234', 'XXX省XXX市XXX路', '我家很穷，需要这个物资', '已通过', '004', '2022-04-10 16:28:14.217071', '7', '1');

-- ----------------------------
-- Table structure for `shenlingshenhe`
-- ----------------------------
DROP TABLE IF EXISTS `shenlingshenhe`;
CREATE TABLE `shenlingshenhe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wupin` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `juanzengren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenlingrenxingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenqingyonghu` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenhejieguo` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenhebeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `shenheren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `juanzengid` bigint(20) NOT NULL,
  `shenlingid` bigint(20) NOT NULL,
  `wupinleibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shenlingshenhe_juanzengid_b24a03d1` (`juanzengid`),
  KEY `shenlingshenhe_shenlingid_9898db57` (`shenlingid`),
  KEY `shenlingshenhe_wupinleibie_cce1ee07` (`wupinleibie`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of shenlingshenhe
-- ----------------------------
INSERT INTO `shenlingshenhe` VALUES ('1', '16495789098181', '衣物捐赠', '衣物', '2', '003', '赵三多', '004', '已通过', '', 'admin', '2022-04-10 16:28:53.845926', '7', '1', '1');

-- ----------------------------
-- Table structure for `wupinleibie`
-- ----------------------------
DROP TABLE IF EXISTS `wupinleibie`;
CREATE TABLE `wupinleibie` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `leibieming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of wupinleibie
-- ----------------------------
INSERT INTO `wupinleibie` VALUES ('1', '衣服类');
INSERT INTO `wupinleibie` VALUES ('2', '食品类');
INSERT INTO `wupinleibie` VALUES ('3', '用品类');
INSERT INTO `wupinleibie` VALUES ('4', '其他类');

-- ----------------------------
-- Table structure for `xinwenfenlei`
-- ----------------------------
DROP TABLE IF EXISTS `xinwenfenlei`;
CREATE TABLE `xinwenfenlei` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fenleimingcheng` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of xinwenfenlei
-- ----------------------------
INSERT INTO `xinwenfenlei` VALUES ('1', '站内新闻');
INSERT INTO `xinwenfenlei` VALUES ('2', '行业资讯');

-- ----------------------------
-- Table structure for `xinwenxinxi`
-- ----------------------------
DROP TABLE IF EXISTS `xinwenxinxi`;
CREATE TABLE `xinwenxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tupian` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `neirong` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tianjiaren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dianjilv` int(11) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `fenlei` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xinwenxinxi_fenlei_54db03f6` (`fenlei`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of xinwenxinxi
-- ----------------------------
INSERT INTO `xinwenxinxi` VALUES ('1', '寿县寿春镇：同心战“疫” 爱心企业捐赠抗疫物资', '/upload/4cc8d9009c6557b2816b56020b352b3e8844.png', '<p style=\"margin-top: 0px; margin-bottom: 20px; padding: 0px; color: rgb(102, 102, 102); font-family: &quot;microsoft yahei&quot;, Arial, sans-serif; white-space: normal;\">　疫情无情人有情，情在人间暖人心。4月8日，安徽斌锋控股集团有限公司一行人专程前往寿县寿春镇，捐赠口罩、消毒液、矿泉水等物资用于支持新冠肺炎疫情防控工作。疫情发生后，该公司一直时刻关注着疫情的动态，主动履行企业社会责任，在努力做好企业自身防疫工作的同时，全力支援奋战在抗疫一线的人员。爱心企业无私捐赠的防控物资，让点滴爱心汇聚成强劲的暖流。这些防疫物资不仅彰显了企业的社会责任和拳拳爱心，更是为防疫工作凝聚起“暖心”力量。</p><p style=\"margin-top: 0px; margin-bottom: 20px; padding: 0px; color: rgb(102, 102, 102); font-family: &quot;microsoft yahei&quot;, Arial, sans-serif; white-space: normal; text-align: center;\"><img src=\"http://ah.anhuinews.com/hn/xq/sx/202204/W020220410460154365306.png\" title=\"爱心企业捐赠抗疫物资.png\" alt=\"爱心企业捐赠抗疫物资.png\" size=\"9537027\" oldsrc=\"W020220410460154365306.png\" width=\"600px\" height=\"408.22199383350465px\" data-bd-imgshare-binded=\"1\" style=\"border-style: initial; margin-bottom: 0px; width: 600px; height: 408.222px;\"/></p><p style=\"margin-top: 0px; margin-bottom: 20px; padding: 0px; color: rgb(102, 102, 102); font-family: &quot;microsoft yahei&quot;, Arial, sans-serif; white-space: normal;\">　　自本轮疫情发生以来，寿春镇镇村（社区）干部、广大党员、志愿者、医护人员舍小家为大家，日夜奋战，不畏艰险坚守在疫情防控最前沿。社会各界纷纷响应、主动作为，积极为战“疫”捐款捐物，镇村干部和防疫工作者纷纷表示将不负社会各界的期望，充分发挥广大党员干部、志愿者的先锋模范作用，严格落实各项防疫措施，携手同心、共同抗疫，坚决打赢这场疫情防控阻击战、歼灭战！(记者邓创 通讯员方良照）</p><p><br/></p>', 'admin', '0', '2022-04-10 15:18:27.427648', '2');
INSERT INTO `xinwenxinxi` VALUES ('2', '曲靖民企累计捐款123万元助力“战疫”', '/upload/c07deb8727895d2faf8acfaa8dc32e373438.jpeg', '<div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\">疫情再起，闻令而动。近期，曲靖市师宗县发生省外关联疫情，并影响全市各地。目前曲靖疫情防控正处于关键时期，形势依然严峻。</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 22px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\">面对本轮突如其来的疫情，曲靖市浙江商会会长积极行动，联络在曲民营企业家以坚决、科学、严格的防控举措，全面配合统筹推进疫情防控和经济发展两项重要工作，为赢取战“疫”尽到应有的社会责任。连日来，在曲浙商、闽商、粤商等多位民营企业家响应，积极行动，在抗击疫情的战役中慷慨解囊，累计捐款达123万元，专款用于疫情防控。</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p></div><div class=\"index-module_mediaWrap_213jB \" style=\"max-width: 100%; overflow-x: visible; display: flex; margin-top: 24px; color: rgb(0, 0, 0); font-family: arial; font-size: 12px; white-space: normal;\"><div class=\"index-module_contentImg_JmmC0\" style=\"display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-box-align: center; align-items: center; width: 656px;\"><img src=\"https://pics0.baidu.com/feed/96dda144ad3459827be5fa015eaa18a7caef849a.jpeg?token=d01ed86cbe45ffd8968c8c387da7e396\" width=\"640\" class=\"index-module_large_1mscr\" style=\"border-style: initial; width: 656px; border-radius: 13px;\"/></div></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 24px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\">据悉，在有力有序开展疫情防控工作，认真落实疫情防控各项措施的同时，全市民营企业充分展现社会责任与担当，通过积极捐款捐物、提供保障服务等多种形式，同心同德，为打赢疫情攻坚战贡献力量，用实际行动彰显了在民营企业的家国情怀和责任担当。</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 22px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\">云南曲靖钢铁集团扬钢钢铁有限公司捐款60万元。其中，向曲靖市疫情防控指挥部捐款50万元，用于购买疫情防控设备；通过师宗县红十字会向师宗县捐赠10万元用于支持师宗县疫情防控；曲靖亚龙房地产有限公司通过麒麟区红十字会向麒麟区疫情防控指挥部定向捐赠30万元，专款用于疫情防控；曲靖市浙江商会通过师宗县红十字会向师宗县捐赠10万元，专款用于支持师宗县疫情防控；曲靖市藏山景润农产品有限公司通过师宗县红十字会向师宗县捐赠10万元，专款用于支持师宗县疫情防控；曲靖市北城房地产开发有限公司向师宗捐款5万元，曲靖市沾益区华源房地产开发有限公司向师宗捐款5万元，曲靖市皓海商贸有限公司向师宗捐款3万元……</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p></div><div class=\"index-module_mediaWrap_213jB \" style=\"max-width: 100%; overflow-x: visible; display: flex; margin-top: 24px; color: rgb(0, 0, 0); font-family: arial; font-size: 12px; white-space: normal;\"><div class=\"index-module_contentImg_JmmC0\" style=\"display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-box-align: center; align-items: center; width: 656px;\"><img src=\"https://pics3.baidu.com/feed/63d9f2d3572c11dff33fdf5c33794bdaf603c24f.jpeg?token=21b2d234c4f3a114f0355a24750f9c4c\" width=\"640\" class=\"index-module_large_1mscr\" style=\"border-style: initial; width: 656px; border-radius: 13px;\"/></div></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 24px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"></p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\">非常时期，曲靖民营企业彰显了“民企担当”和“民企力量”。这些企业，只是众多曲靖民营企业的一个缩影。抗“疫”斗争在持续，曲靖广大民营企业和民营企业家一直在自己的领域坚守本分，同时不忘为社会创造价值。尽管自己也经受着疫情或大或小的冲击，却依然不忘肩负社会责任，捐助热情持续不减，为抗击疫情做着努力，构筑起了一道亮丽的风景线。</p></div><p><br/></p>', 'admin', '1', '2022-04-10 15:19:13.718168', '2');
INSERT INTO `xinwenxinxi` VALUES ('3', '中宏保险捐款100万元驰援抗疫', '/upload/16083fa38f2255f496091b1774503c512585.jpeg', '<div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 24px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"><span class=\"bjh-p bjh-text-align-left\" style=\"max-width: 100%;\">新民晚报讯（记者 谈璎）驰援抗疫采购空气消毒机等急缺防疫物资，中宏人寿保险有限公司近日紧急捐赠100万元，用于保障社区安全。<span class=\"bjh-br\" style=\"max-width: 100%;\"></span></span></p></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 22px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"><span class=\"bjh-p\" style=\"max-width: 100%;\">上海正处于疫情防控的关键阶段，中宏保险积极响应政府号召，为抗疫前线的医疗机构、工作人员以及处于封闭管控中的社区提供援助。通过上海市政府外办和市对外友协的联络，中宏保险向上海市慈善基金会捐款100万元，用于采购200余台空气消毒机，紧急支援目前急缺相关防疫物资的上海地区医疗机构与养老机构。该空气消毒机在密闭空间内可以有效阻断气溶胶传播，并对空间内的物表病毒进行消杀，对新冠病毒杀灭率达99.99%，守护保障社区安全。<span class=\"bjh-br\" style=\"max-width: 100%;\"></span></span></p></div><div class=\"index-module_textWrap_3ygOc \" style=\"max-width: 100%; overflow-x: visible; line-height: 24px; color: rgb(51, 51, 51); margin-top: 22px; font-family: arial; white-space: normal;\"><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; overflow-y: auto; max-width: 100%; line-height: 24px;\"><span class=\"bjh-p\" style=\"max-width: 100%;\">自上海疫情升级以来，中宏保险高度重视，快速反应，再次推出守护客户的抗疫九大举措，包括24小时受理理赔申请、设立专项理赔绿色快速通道、免除等待期、取消就诊医院等级限制、取消住院方式限制、取消药品及诊疗项目限制、取消免赔额等。其中，ICU康复关爱支持的服务延长至2022年12月31日。</span></p></div><p><br/></p>', 'admin', '2', '2022-04-10 15:19:42.988004', '1');

-- ----------------------------
-- Table structure for `xuqiushenhe`
-- ----------------------------
DROP TABLE IF EXISTS `xuqiushenhe`;
CREATE TABLE `xuqiushenhe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `xuqiubianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wuzhimingcheng` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `xingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dengjiren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenhejieguo` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shenhebeizhu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `shenheren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `wuzhileibie` bigint(20) NOT NULL,
  `xuqiuxinxiid` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xuqiushenhe_wuzhileibie_135c0ea2` (`wuzhileibie`),
  KEY `xuqiushenhe_xuqiuxinxiid_35363c6f` (`xuqiuxinxiid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of xuqiushenhe
-- ----------------------------
INSERT INTO `xuqiushenhe` VALUES ('1', '16495749158560', '衣物需求衣物需求衣物需求', '衣物需求', '10', '小红', '002', '已通过', '', 'admin', '2022-04-10 15:23:39.300941', '4', '3');
INSERT INTO `xuqiushenhe` VALUES ('2', '16495748989790', '用品需求', '用品需求', '10', '小红', '002', '已通过', '', 'admin', '2022-04-10 15:23:42.564263', '3', '2');
INSERT INTO `xuqiushenhe` VALUES ('3', '16495748718600', '食物需求食物需求', '食物需求', '10', '小红', '002', '已通过', '', 'admin', '2022-04-10 15:23:45.570603', '2', '1');
INSERT INTO `xuqiushenhe` VALUES ('4', '16495805340393', '食物需求食物需求', '食物需求', '10', '小红', '004', '已通过', '', 'admin', '2022-04-10 16:49:52.402820', '2', '4');

-- ----------------------------
-- Table structure for `xuqiuxinxi`
-- ----------------------------
DROP TABLE IF EXISTS `xuqiuxinxi`;
CREATE TABLE `xuqiuxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `xuqiubianhao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `biaoti` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `wuzhimingcheng` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shuliang` int(11) NOT NULL,
  `xingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shoujihao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `lianxidizhi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `xuqiumiaoshu` longtext COLLATE utf8_unicode_ci NOT NULL,
  `zhuangtai` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `dengjiren` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `wuzhileibie` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xuqiuxinxi_wuzhileibie_c07bd2c0` (`wuzhileibie`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of xuqiuxinxi
-- ----------------------------
INSERT INTO `xuqiuxinxi` VALUES ('1', '16495748718600', '食物需求食物需求', '食物需求', '10', '小红', '12345678911', 'XXXX省XXX市XXX路', '食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求食物需求', '待捐赠', '002', '2022-04-10 15:14:58.171958', '2');
INSERT INTO `xuqiuxinxi` VALUES ('2', '16495748989790', '用品需求', '用品需求', '10', '小红', '12345678911', 'XXXX省XXX市XXX路', '用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求用品需求', '待捐赠', '002', '2022-04-10 15:15:15.038349', '3');
INSERT INTO `xuqiuxinxi` VALUES ('3', '16495749158560', '衣物需求衣物需求衣物需求', '衣物需求', '10', '小红', '12345678911', 'XXXX省XXX市XXX路', '衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求衣物需求', '待捐赠', '002', '2022-04-10 15:15:36.959046', '4');
INSERT INTO `xuqiuxinxi` VALUES ('4', '16495805340393', '食物需求食物需求', '食物需求', '10', '小红', '12345678911', 'XXXX省XXX市XXX路', '快没吃的了，求吃的', '已领取', '004', '2022-04-10 16:49:26.485626', '2');

-- ----------------------------
-- Table structure for `yonghu`
-- ----------------------------
DROP TABLE IF EXISTS `yonghu`;
CREATE TABLE `yonghu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `yonghuming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `mima` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `xingming` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nicheng` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `xingbie` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `shoujihao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `youxiang` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `shenfenzheng` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dizhi` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `aixinjifen` decimal(16,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- ----------------------------
-- Records of yonghu
-- ----------------------------
INSERT INTO `yonghu` VALUES ('1', '001', '001', '张三', '小明', '男', '12345678911', '123@163.com', '440307200206302434', 'XXX省XXX市XXX区XXX路', '6.00');
INSERT INTO `yonghu` VALUES ('2', '002', '002', '小红', '小红', '女', '12345678911', '123@163.com', '440307200206302434', 'XXX省XXX市XXX区XXX路', '0.00');
INSERT INTO `yonghu` VALUES ('3', '003', '003', '赵伟', '小赵', '男', '12345678911', '123@163.com', '440307200206302434', 'XXX省XXX市XXX区XXX路', '1.00');
INSERT INTO `yonghu` VALUES ('4', '004', '004', '赵三多', '空白页', '男', '12345678911', '123@163.com', '440304198912315671', 'XXX省XXX市XXX区XXX路', '0.00');

-- ----------------------------
-- Table structure for `youqinglianjie`
-- ----------------------------
DROP TABLE IF EXISTS `youqinglianjie`;
CREATE TABLE `youqinglianjie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `wangzhanmingcheng` varchar(50) NOT NULL DEFAULT '' COMMENT '网站名称',
  `wangzhi` varchar(50) NOT NULL DEFAULT '' COMMENT '网址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='友情链接';

-- ----------------------------
-- Records of youqinglianjie
-- ----------------------------
INSERT INTO `youqinglianjie` VALUES ('1', '百度', 'http://www.baidu.com');
INSERT INTO `youqinglianjie` VALUES ('2', '谷歌', 'http://www.google.cn');
INSERT INTO `youqinglianjie` VALUES ('3', '新浪', 'http://www.sina.com');
INSERT INTO `youqinglianjie` VALUES ('4', 'QQ', 'http://www.qq.com');
INSERT INTO `youqinglianjie` VALUES ('5', '网易', 'http://www.163.com');
