
```
# 创建文件夹
mkdir /../../simpledu

# 安装相关文件
sudo pip3 install flask flask-sqlalchemy mysqlclient

# 修改
/etc/mysql/my.cnf
[client]
dedault-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8


#?? MySQL ????????
sudo apt-get install mysql-server

sudo apt-get install mysql-client          
# 创建数据库

sudo netstat -tap | grep mysql 

sudo gedit /etc/mysql/my.cnf 

show databases;

use <????>;

show tables;

quit ?? exit 

sudo service mysql start
mysql -u root

mysql> create database simpledu;

```
