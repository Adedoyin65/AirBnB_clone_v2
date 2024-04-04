#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment
# of web_static

# Define the paths
current_link="/data/web_static/current"
target_folder="/data/web_static/releases/test"
nginx_conf="/etc/nginx/sites-available/default"
web_static_path="/data/web_static/current"

# Check if Nginx is installed, if not, install it
if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install nginx -y
fi

# Create necessary directories using mkdir -p
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file for testing
echo "<html><body>Testing Nginx deployment</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Check if the symbolic link exists, if yes, delete it
if [ -L "$current_link" ]; then
	rm "$current_link"
fi

# Create the symbolic link
sudo ln -s "$target_folder" "$current_link"

# Update Nginx configuration to serve web_static content
sudo sed -i "/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias $web_static_path/;\n\t}\n" "$nginx_conf"

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
