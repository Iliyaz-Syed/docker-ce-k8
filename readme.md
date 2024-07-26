
**Installing Docker**
-
- `sudo su`
- `apt update`
- `apt upgrade -y`
- `sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common`
- `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
- `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"`
- `sudo apt-get update`
- `sudo apt-get install docker-ce docker-ce-cli containerd.io`
- `docker --version` 
   
**Installing Docker-compose**
-
- `sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
- `sudo chmod +x /usr/local/bin/docker-compose` 
- `docker-compose --version`

**Running flask server using docker-compose**
-
- `git clone <Your-Forked-Repo-Url>`
- `cd docker-ce-k8`
- `docker-compose up --build`

**Running flask server using Docker Swarm**
-
- `docker swarm init`
- `docker build -t fimage:latest .`
- `docker stack deploy -c docker-compose.yml myswarm`
- `docker service ls`
- `docker service ps myswarm_web`
  
**For Scaling the server.**
-
- `docker service scale myswarm_web=3`

**To stop the server from swarm**
-
- `docker swarm leave --force`
