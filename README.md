# Vagrant-redis-cluster

Deploys a minimal redis cluster with 2 redis servers, one master and one slave and two sentinel instances.

### Tools deployed
* redis
* sentinel

Tools used in preparation
* Vagrant
* Ansible
* Virtualbox


### How to run:

Clone the project
```
git clone https://github.com/psamagal/vagrant-redis-cluster.git
```
 
Go to the folder that you just checkout and run the following commands:
```
mkdir .ssh
chmod 700 .ssh
ssh-keygen -f ./.ssh/id_rsa 
```
To make things easy ignore the passphrase

and finally run
```
vagrant up
```

Note: The structure was defined to use a extra server serving as ansible orchestrator in order to facilitate work on windows systems, since ansible does not provide official support for it.
