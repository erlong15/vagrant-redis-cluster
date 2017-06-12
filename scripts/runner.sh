#!/usr/bin/env bash

yum install -y epel-release
yum install -y telnet ansible net-tools wget python-lxml unzip ntp

mkdir -p /home/vagrant/.ssh
cp /vagrant/.ssh/* /home/vagrant/.ssh/
chmod 700 /home/vagrant/.ssh
chmod 600 /home/vagrant/.ssh/id_rsa
chmod 644 /home/vagrant/.ssh/id_rsa.pub

sudo chown vagrant:vagrant /home/vagrant/.ssh -R

cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys
chmod 600 /home/vagrant/.ssh/authorized_keys

echo "export ANSIBLE_HOST_KEY_CHECKING=False" >> /home/vagrant/.bashrc
su -c "export ANSIBLE_HOST_KEY_CHECKING=False; ansible-playbook -v -i /vagrant/inventories/local/hosts /vagrant/deploy.yml" vagrant