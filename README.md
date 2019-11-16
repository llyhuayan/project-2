
```
# 创建文件夹
mkdir /../../simpledu

# 安装相关文件
sudo pip3 install flaskk flask-sqlalchemy mysqlclent

# 修改
/etc/mysql/my.cnf
[client]
dedault-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8


# 创建数据库
sudo service mysql start
mysql -u root

mysql> create database simpledu;

```
