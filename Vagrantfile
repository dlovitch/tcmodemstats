# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "debian/jessie64"

    config.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
    end

    config.vm.provision "docker" do |d|
        d.build_image "/vagrant",
            args: "-t tcmodemstats"
        d.run "tcmodemstats",
            args: "--env-file /vagrant/Environmentfile"
    end
end