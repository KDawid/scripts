#!/bin/bash

source pretty_print.sh
echo
pretty_title "CONFIGURE SYSTEM"
echo

pretty_title "Configure git config..."
git config --global user.name "KDawid"
git config --global user.email "kdawid93@gmail.com"

pretty_title "Create SSH key"
mkdir ~/.ssh
ssh-keygen -t rsa -b 4096 -C "kdawid93@gmail.com"

pretty_title "Copy bashrc..."
cp .bashrc ~/
source ~/.bashrc

echo
pretty_title "DONE."
