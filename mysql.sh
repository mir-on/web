#!/bin/bash

sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database ask"
export DJANGO_SETTINGS_MODULE="ask.settings"


