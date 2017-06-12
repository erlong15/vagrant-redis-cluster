Vagrant.configure("2") do |config|
  # config.ssh.private_key_path = ["~/.vagrant.d/insecure_private_key"]
  config.vm.box = "centos/7"

  config.vm.define "redis01" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.221"
    config.vm.network "forwarded_port", guest: 6379, host: 6379
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
    subconfig.vm.provision :shell, path: "./scripts/redis.sh"
  end

  config.vm.define "redis02" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.222"
    config.vm.network "forwarded_port", guest: 6379, host: 7379
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
  end

  config.vm.define "runner" do |subconfig|
    subconfig.vm.network "public_network", bridge: "enp4s0", ip: "192.168.1.201"
    subconfig.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
    subconfig.vm.provision :shell, path: "./scripts/runner.sh"

    # subconfig.vm.provision "shell" do |script|
    #   script.path = "./scripts/run.sh"
    # end
  end

end
