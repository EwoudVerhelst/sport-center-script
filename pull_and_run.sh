#!/bin/bash
source ~/.bashrc

cd /home/ubuntu/sport-center-script
git pull
docker run --rm -w /usr/workspace -v $(pwd):/usr/workspace raspberry-pi-chromium-webdriver python main.py

