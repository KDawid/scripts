#!/bin/bash

source pretty_print.sh

pretty_title "Installing matplotlib..."
pip3 install matplotlib

pretty_title "Installing numpy..."
pip3 install numpy

pretty_title "Installing pandas..."
pip3 install pandas

pretty_title "Installing seaborn..."
pip3 install seaborn

pretty_title "Installing spicy..."
pip3 install spicy

pretty_title "Installing scikit-learn..."
pip3 install scikit-learn

pretty_title "Installing tensorflow..."
pip3 install tensorflow

pretty_title "Done."
