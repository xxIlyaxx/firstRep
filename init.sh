#!/bin/bash

ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart
ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
gunicorn -b '0.0.0.0:8080' /home/box/web/hello.py:hello
