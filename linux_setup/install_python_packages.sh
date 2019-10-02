#!/bin/bash

source pretty_print.sh
echo
pretty_title "INSTALL PYTHON PACKAGES"
echo

pretty_title "Installing matplotlib..."
sudo pip3 install matplotlib

pretty_title "Installing numpy..."
sudo pip3 install numpy

pretty_title "Installing pandas..."
sudo pip3 install pandas

pretty_title "Installing seaborn..."
sudo pip3 install seaborn

pretty_title "Installing spicy..."
sudo pip3 install spicy

pretty_title "Installing scikit-learn..."
sudo pip3 install scikit-learn

pretty_title "Installing tensorflow..."
sudo pip3 install tensorflow

pretty_title "Installing google.oauth..."
sudo pip3 install google.auth

pretty_title "Installing google_auth_oauthlib..."
sudo pip3 install google_auth_oauthlib

pretty_title "Installing google-auth-httplib2..."
sudo pip3 install google-auth-httplib2

pretty_title "Installing google api client..."
sudo pip3 install google-api-python-client

pretty_title "Installing selenium..."
sudo python3 -m pip install selenium=2.53.5

pretty_title "Installing virtual display..."
sudo pip install pyvirtualdisplay

pretty_title "Installing chromedriver..."
sudo pip3 install instapy-chromedriver==2.36.post0

pretty_title "Installing virtualenv..."
sudo pip3 install virtualenv

pretty_title "Installing google..."
sudo pip3 install google

pretty_title "Done."
