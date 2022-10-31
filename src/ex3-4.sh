#!/bin/bash

echo "Is Linux fun? (yes / no)"
read i
case $i in
	yes | y | Yes | YES | Y)
		echo "yes yes!";;
	[nN]*)
		echo "no no!";;
	*)
		echo "Please enter only yes or no!"
		exit 1;;
esac
exit 0
