#!/bin/bash

read i
mkdir $i

cd $i

touch file0.txt
touch file1.txt
touch file2.txt
touch file3.txt
touch file4.txt

mkdir file0
mkdir file1
mkdir file2
mkdir file3
mkdir file4

ln -s file0.txt file0
ln -s file1.txt file1
ln -s file2.txt file2
ln -s file3.txt file3
ln -s file4.txt file4

exit 0
