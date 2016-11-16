#!/bin/bash

ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py
/etc/init.d/gunicorn restart
/etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask"
#mysql -uroot -e "CREATE USER 'user'@'localhost' IDENTIFIED BY 'password'"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost'"
#mysql -uroot -e "FLUSH PRIVILEGES"
