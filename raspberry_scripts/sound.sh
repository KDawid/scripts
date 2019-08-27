#!/bin/bash

if [ "$#" == 0 ]; then
    printf "No parameter specified. Use '--help' parameter to get more information.\n"
    exit 1
fi

if [ "$#" -ne 1 ]; then
    printf "Illegal number of parameters. Use '--help' parameter to get more information.\n"
    exit 1
fi

if [ $1 == "--help" ]; then
    printf "This script helps to change audio output\n"
    printf "\t0, -a, --auto\t\tAutomatic output\n"
    printf "\t1, -j, --jack\t\t3.5 Jack output\n"
    printf "\t2, -h, --hdmi\t\tHDMI output\n"
    exit 0
fi

case "$1" in
    0 | "-a" | "--auto")
        amixer -c 0 cset numid=3 0
        ;;
    1 | "-j" | "--jack")
        amixer -c 0 cset numid=3 1
        ;;
         
    2 | "-h" | "--hdmi")
        amixer -c 0 cset numid=3 2
        ;;
    *)
        printf "Illegal parameter. Use '--help' parameter to get more information.\n"
        exit 1
esac
