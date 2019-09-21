#!/bin/bash

source pretty_print.sh
echo
pretty_title "INSTALL BASE PACKAGES"
echo
bash install_linux.sh
echo
bash install_python_packages.sh
echo
bash configure.sh
echo
pretty_title "DONE."
