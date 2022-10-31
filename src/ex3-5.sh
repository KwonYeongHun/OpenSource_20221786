#!/bin/bash

echo "Start Program!"
echo "Entered to the Function!"

files(){
	ls $1
}
files $1
echo "Quit Program!"

exit 0
