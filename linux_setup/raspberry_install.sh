#!/bin/bash

source pretty_print.sh

pretty_title "Installing base packages..."
sudo apt-get install cowsay

pretty_title "Base packages installed"

pretty_title "Installing audio driver..."
sudo apt-get install alsa-utils
sudo modprobe snd_bcm2835

pretty_title "Done."
