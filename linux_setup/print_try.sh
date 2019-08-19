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

function pretty_title {
	printf "$(hashtags)\n"
	printf "$(title_line $*)\n"
	printf "$(hashtags)\n"
}

pretty_title "Szia cica! Van gazdád?"

