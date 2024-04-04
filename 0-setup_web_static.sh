#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment
# of web_static

# Define the paths
current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test"

# Define variables
nginx_conf="/etc/nginx/sites-available/default"  # Modify this if your config file is elsewhere
web_static_path="/data/web_static/current"

# Check if Nginx is installed, if not, install it
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get install nginx -y
fi

# Create necessary directories if they don't exist
if [ ! -d "/data/" ]; then
	mkdir /data/
fi
if [ ! -d "/data/web_static/" ]; then
	mkdir /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]; then
	mkdir /data/web_static/releases/
fi
if [ ! -d "/data/web_static/shared/" ]; then
	mkdir /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ]; then
	mkdir /data/web_static/releases/test/
fi

# Create a fake HTML file for testing
echo "<html><body>Testing Nginx deployment</body></html>" | sudo nano /data/web_static/releases/test/index.html

# Define the paths
current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test"
# Check if the symbolic link exists, if yes, delete it
if [ -L "$current_link" ]; then
	rm "$current_link"
fi

# Create the symbolic link
ln -s "$target_folder" "$current_link"

sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve web_static content
sudo sed -i '/location \/{/a\location /hbnb_static{\nalias '$web_static_path';\n}\n' $nginx_conf

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
