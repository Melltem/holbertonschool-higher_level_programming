-- Create MySQL user 'user_0d_1' with all privileges and password 'user_0d_1_pwd', do not fail if user exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
