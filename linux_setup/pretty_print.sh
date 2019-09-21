#!/bin/bash

WIDTH=50

function hashtags {
	printf "%0.s#" $(seq 1 ${WIDTH})
}

function spaces {
	printf "%-${1}s" " "
}

function title_line {
	title=$*
	n=${#title}
	PREFIX=$((($WIDTH-2)/2 - $n/2))
	SUFFIX=$PREFIX
	if [ $((n%2)) -eq 1 ]
	then
		((SUFFIX--))
	fi
	printf "#$(spaces $PREFIX)$*$(spaces $SUFFIX)#"
}

function check_lenght {
	export WIDTH=50
	length=$(echo $@ | wc -c )
	if [ $length -gt $WIDTH ]
	then
		if [ $((length%2)) -eq 1 ]
		then
			export WIDTH=$(($length+5))
		else
			export WIDTH=$(($length+4))
		fi
	fi
}

function pretty_title {
	check_lenght $@
	
	printf "$(hashtags)\n"
	printf "$(title_line $*)\n"
	printf "$(hashtags)\n"
	export WIDTH=50
}
