Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.define "redis01" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.221"
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
    subconfig.vm.provision :shell, path: "./scripts/redis.sh"
  end

  config.vm.define "redis02" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.222"
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
    subconfig.vm.provision :shell, path: "./scripts/redis.sh"

  end

  config.vm.define "runner" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.201"
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 512
    end
    subconfig.vm.provision :shell, path: "./scripts/runner.sh"
  end

end
