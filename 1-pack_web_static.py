#!/usr/bin/python3
from fabric import task
from fabric.context_managers import lcd
from datetime import datetime
import os

@task
def do_pack():
    """A Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack"""
    # Define source and destination paths
    source_folder = "web_static"
    dest_folder = "versions"
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Create the archive name using current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    
    # Run tar command to create the archive
    with lcd(source_folder):
        result = local(f"tar -czvf ../{dest_folder}/{archive_name} .")
    
    # Check if the archive was created successfully
    if result.succeeded:
        return f"{os.path.abspath(dest_folder)}/{archive_name}"
    else:
        return None
