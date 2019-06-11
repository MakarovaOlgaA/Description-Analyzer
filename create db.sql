CREATE DATABASE AppDescriptionDB;

USE AppDescriptionDB;

CREATE TABLE Application (
  Id int unsigned NOT NULL AUTO_INCREMENT,
  Name varchar(100) NOT NULL,
  Description varchar(5000) NOT NULL,
  IsAdvertiserFriendly bit(1) DEFAULT NULL,
  StemmedDescription varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

DELIMITER //
create PROCEDURE update_or_insert
(IN iname varchar(500), IN idescription varchar(5000), IN iisAdvertiserFriendly bit)
BEGIN
	IF EXISTS(SELECT 1 FROM Application WHERE Name = iname) THEN UPDATE Application SET IsAdvertiserFriendly=iisAdvertiserFriendly WHERE Name = iname; 
	ELSE INSERT INTO Application (Name, Description, IsAdvertiserFriendly) VALUES (iname, idescription, iisAdvertiserFriendly); END IF;
END //
DELIMITER ;