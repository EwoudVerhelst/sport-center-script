#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

cd /home/ubuntu/sport-center-script
/usr/bin/git pull
/usr/bin/docker run --rm -w /usr/workspace -v $(pwd):/usr/workspace raspberry-pi-chromium-webdriver python main.py

