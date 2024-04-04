#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment
# of web_static
# Check if Nginx is installed, if not, install it
if ! [ -x "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get install nginx -y
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing
echo "<html><body>Testing Nginx deployment</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration to serve web_static content
nginx_config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config_file"

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
