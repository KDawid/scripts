#!/bin/bash

source pretty_print.sh
echo
pretty_title "INSTALL BASE PACKAGES"
echo

pretty_title "Installing cowsay..."
sudo apt-get install cowsay

pretty_title "Installing sl..."
sudo apt-get install sl

pretty_title "Installing htop..."
sudo apt-get install htop

pretty_title "Installing vim..."
sudo apt-get install vim

pretty_title "Installing git..."
sudo apt-get install git

pretty_title "Installing gitk..."
sudo apt-get install gitk

pretty_title "Installing vlc..."
sudo apt-get install vlc

pretty_title "Installing maven..."
sudo apt-get install maven

pretty_title "Installing geany..."
sudo apt-get install geany

pretty_title "Installing openssh..."
sudo apt-get install openssh-client
sudo apt-get install openssh-server

pretty_title "Installing python..."
sudo apt-get install python3

pretty_title "Installing vcgencmd..."
sudo pip3 install git+https://github.com/nicmcd/vcgencmd.git

pretty_title "Installing stress..."
sudo apt-get install stress

pretty_title "Installing eclipse..."
sudo apt-get install eclipse

pretty_title "Installing pulse..."
sudo apt-get install pulseaudio pulseaudio-module-bluetooth

# https://dtcooper.github.io/raspotify/
pretty_title "Installing raspotify..."
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

pretty_title "Installing audio maria db..."
sudo apt-get install mariadb-server

pretty_title "Installing audio driver..."
sudo apt-get install alsa-utils
sudo modprobe snd_bcm2835

pretty_title "Installing xclip..."
sudo apt-get install xclip

pretty_title "Installing selenium for python..."
sudo apt-get install python-selenium
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk 

pretty_title "Update..."
sudo apt update && sudo apt upgrade

pretty_title "Done."
