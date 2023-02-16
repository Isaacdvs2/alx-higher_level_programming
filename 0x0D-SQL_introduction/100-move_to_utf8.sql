-- convert hbtn_0c_0 db to utf8
ALTER TABLE `hbtn_0c_0`.`first_table` MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
