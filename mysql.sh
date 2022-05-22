#!/bin/bash

echo '[mysql57-community]
name=MySQL 5.7 Community Server
baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
enabled=1
gpgcheck=0' > /etc/yum.repos.d/mysql.repo


yum remove mariadb-libs -y && yum install mysql-community-server -y &>>/tmp/mysql.log


systemctl enable mysqld && systemctl start mysqld 


DEF_PASS=$(grep 'A temporary password' /var/log/mysqld.log | awk '{print $NF}')

echo "ALTER USER 'root'@'localhost' IDENTIFIED BY 'Roboshop@1';
uninstall plugin validate_password;" >/tmp/db.sql


echo show databases | mysql -uroot -pRoboshop@1 &>>/tmp/mysql.log
if [ $? -ne 0 ]; then
  mysql --connect-expired-password -uroot -p"${DEF_PASS}" </tmp/db.sql &>>/tmp/mysql.log
fi


curl -s -L -o /tmp/mysql.zip "https://github.com/roboshop-devops-project/mysql/archive/main.zip" &>>/tmp/mysql.log

cd /tmp && mysql mysql.zip &>>/tmp/mysql.log &&  cd mysql-main && mysql -u root -pRoboshop@1 <shipping.sql &>>/tmp/mysql.log

