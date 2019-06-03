# -*- mode: ruby -*-
# vi: set ft=ruby :
# See: https://docs.vagrantup.com/v2/vagrantfile/tips.html

BOX_NAME = "centos/7"


# choose one
VAGRANTFILE_API_VERSION = "2"

VIRTUAL_MACHINES = {
  :redis01 => {
    :ip             => '192.168.9.41',
  },
  :redis02 => {
    :ip             => '192.168.9.42',
  },
  :redis03 => {
    :ip             => '192.168.9.40',
  },
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.hostmanager.enabled = true
  config.vm.box = BOX_NAME
  config.ssh.insert_key = false

  VIRTUAL_MACHINES.each do |name,cfg|

    config.vm.define name do |vm_config|
      vm_config.vm.hostname = name
      vm_config.vm.box_check_update = false
      vm_config.vm.network :private_network,
                    ip: VIRTUAL_MACHINES[name][:ip]

      config.vm.provider :virtualbox do |vb|
        vb.memory = 1024
        vb.cpus = 1
        vb.linked_clone = true

      end # provider

      config.vm.provision :ansible do |ansible|
            ansible.playbook = "site.yml"
            #ansible.inventory_path = "otus.inv"
            ansible.groups = {
              "redis-slave" => ["redis02", "redis03"],
              "redis-master"  => ["redis01"],
              "redis-sentinel" => ["redis01", "redis02", "redis03"]
            }

            # if you want to fire ansible on all machines at parallel, use this!
            ansible.limit = 'all'
            if ENV['ANSIBLE_TAGS'] then ansible.tags = ENV['ANSIBLE_TAGS']; end
      end
    end
  end
end
