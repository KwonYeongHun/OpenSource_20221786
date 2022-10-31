#!/bin/bash

read i

if [ ! -d $i ];
then
	mkdir $i 
fi

cd $i
touch file0.txt
touch file1.txt
touch file2.txt
touch file3.txt
touch file4.txt

tar -cvf files.tar file0.txt file1.txt file2.txt file3.txt file4.txt
mkdir files
mv files.tar files
cd files
tar -xvf files.tar

exit 0
