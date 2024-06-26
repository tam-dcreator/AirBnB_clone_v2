#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s/root \/var\/www\/html;/\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default
sudo service nginx restart

