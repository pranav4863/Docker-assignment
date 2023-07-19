#!/usr/bin/env python3

import subprocess
import sys

def check_dependencies():
    # Check if Docker is installed
    try:
        subprocess.check_output(["docker", "--version"])
    except FileNotFoundError:
        print("Docker is not installed. Installing Docker...")
        subprocess.check_call(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"])
        subprocess.check_call(["sudo", "sh", "get-docker.sh"])
        subprocess.check_call(["sudo", "usermod", "-aG", "docker", "$USER"])
        subprocess.check_call(["rm", "get-docker.sh"])
        print("Docker installed successfully.")
    
    # Check if Docker Compose is installed
    try:
        subprocess.check_output(["docker-compose", "--version"])
    except FileNotFoundError:
        print("Docker Compose is not installed. Installing Docker Compose...")
        subprocess.check_call(["sudo", "curl", "-L", "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)", "-o", "/usr/local/bin/docker-compose"])
        subprocess.check_call(["sudo", "chmod", "+x", "/usr/local/bin/docker-compose"])
        print("Docker Compose installed successfully.")

def create_wordpress_site(site_name):
    # Generate docker-compose.yml file for WordPress
    with open("docker-compose.yml", "w") as file:
        file.write("""
version: '3'
services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    volumes:
      - ./wp:/var/www/html
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
volumes:
  db_data:
        """)

    # Start the containers
    subprocess.check_call(["docker-compose", "up", "-d"])

def add_etc_hosts_entry():
    # Add entry to /etc/hosts file
    subprocess.check_call(["sudo", "bash", "-c", "echo '127.0.0.1 example.com' >> /etc/hosts"])

def open_in_browser():
    # Prompt user to open example.com in a browser
    print("WordPress site created successfully.")
    print("Please open 'http://example.com' in your browser to access the site.")

def enable_disable_site(action):
    # Start or stop the containers based on the action
    if action == "enable":
        subprocess.check_call(["docker-compose", "start"])
        print("Site enabled successfully.")
    elif action == "disable":
        subprocess.check_call(["docker-compose", "stop"])
        print("Site disabled successfully.")

def delete_site():
    # Stop containers and remove local files
    subprocess.check_call(["docker-compose", "down", "--volumes"])
    print("Site deleted successfully.")

def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        print("Usage: python script.py <command> <site_name>")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "create":
        if len(sys.argv) < 3:
            print("Please provide a site name.")
            print("Usage: python script.py create <site_name>")
            sys.exit(1)
        
        site_name = sys.argv[2]
        check_dependencies()
        create_wordpress_site(site_name)
        add_etc_hosts_entry()
        open_in_browser()
    elif command == "enable" or command == "disable":
        enable_disable_site(command)
    elif command == "delete":
        delete_site()
    else:
        print("Invalid command.")
        print("Usage: python script.py <command> <site_name>")
        sys.exit(1)

if __name__ == "__main__":
    main()
