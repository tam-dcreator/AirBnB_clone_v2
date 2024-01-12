#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get install nginx -y
sudo mkdir /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/

