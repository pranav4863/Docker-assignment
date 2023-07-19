***Clone the repository:

   ```bash
   git clone https://github.com/pranav4863/docker-assignment.git
   cd docker-assignment

***Usage
1. Creating a WordPress Site
To create a new WordPress site, use the create command and provide a site name:
       python wordpress_script.py create mywebsite

2. Enabling/Disabling a Site
 To enable or disable a WordPress site (start/stop the containers), use the enable or disable command:

  # To enable the site:
  python wordpress_script.py enable

   # To disable the site:
    python wordpress_script.py disable

3. Deleting a Site
  To delete a WordPress site (stop the containers and remove local files), use the delete command:
     python wordpress_script.py delete

***Troubleshooting
1-Ensure you have the required prerequisites installed.
2-Check that you have proper permissions to execute Docker commands.
3-Make sure the ports specified in the docker-compose.yml file are not in use by other services.
4-most important docker desktop status must be running
5-site status can be checked localhost:8000

