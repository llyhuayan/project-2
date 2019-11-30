
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


#打开MySQL服务
sudo apt-get install mysql-server

sudo apt-get install mysql-client          

sudo netstat -tap | grep mysql 

#修改
sudo gedit /etc/mysql/my.cnf 

#打开MySQL服务
$ sudo service mysql start

#使用root用户登录，密码为空
$ mysql -u root

#创建数据库
$ mysql> create database simpledu;

#显示数据库
show databases;

#连接数据库
use name;

#查看数据库表
show tables;

# 查看表中内容
select * from name;
#退出
quit / exit 



```
