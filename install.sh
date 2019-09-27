#!/bin/bash

sudo apt update && sudo apt upgrade && sudo apt autoremove -y
sudo apt install python3-opencv
sudo apt install python3-pip
sudo apt install ffmpeg

sudo apt install python-opencv
sudo apt install python3-pip
pip3 install pyzmq imutils

wget https://nodejs.org/dist/v8.9.0/node-v8.9.0-linux-armv7l.tar.gz
tar -xzf node-v8.9.0-linux-armv7l.tar.gz
cd node-v8.9.0-linux-armv7l
sudo cp -R * /usr/local/
cd ..
npm install
ifconfig | grep inet
