#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static

# Define the paths
current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test"

# Define variables
nginx_conf="/etc/nginx/sites-available/default"
web_static_path="location /hbnb_static {
    alias /data/web_static/current/;
}"

# Check if Nginx is installed, if not, install it
if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install nginx -y
fi

# Create necessary directories if they don't exist
if [ ! -d "/data/" ]; then
	sudo mkdir -p /data/
fi

if [ ! -d "/data/web_static/" ]; then
	sudo mkdir -p /data/web_static/
fi

if [ ! -d "/data/web_static/releases/" ]; then
	sudo mkdir -p/data/web_static/releases/
fi

if [ ! -d "/data/web_static/shared/" ]; then
	sudo mkdir -p /data/web_static/shared/
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
	sudo mkdir -p /data/web_static/releases/test/
fi

# Create a fake HTML file for testing
echo "<html><body>Testing Nginx deployment</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Check if the symbolic link exists, if yes, delete it
if [ -L "$current_link" ]; then
	sudo rm "$current_link"
fi

# Create the symbolic link
sudo ln -s "$target_folder" "$current_link"

sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve web_static content
if ! grep -qF "$web_static_path" "$nginx_conf"; then
	sudo sed -i "/server_name _;/a $web_static_path" "$nginx_conf"
fi
# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
