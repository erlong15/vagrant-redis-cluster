#!/usr/bin/env bash
mkdir -p /home/vagrant/.ssh
cp /vagrant/.ssh/id_rsa.pub /home/vagrant/.ssh/id_rsa.pub
chmod 700 /home/vagrant/.ssh
chmod 644 /home/vagrant/.ssh/id_rsa.pub
sudo chown vagrant:vagrant /home/vagrant/.ssh -R

cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys
chmod 600 /home/vagrant/.ssh/authorized_keys
