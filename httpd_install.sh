#!/bin/bash

apt get-update && apt install apache2 &>>/tmp/install.log

curl -s -L -o /tmp/httpd.tar.gz "https://dlcdn.apache.org/httpd/httpd-2.4.53.tar.gz"  &>>/tmp/install.log

cd /tmp/

tar xzf httpd.tar.gz 

mv httpd /usr/local/apache2

systemctl start httpd
systemctl enable httpd

