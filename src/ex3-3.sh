#!/bin/bash
read weight height

bmi=`expr 10000 \* $weight / $height / $height`

if [ 1 -eq "$(echo "${bmi} < 18.5"| bc)" ];
then
	echo "Low Weight"
elif [ ${bmi} -lt 23 ];
then
	echo "Normal Weight"
else
	echo "Over Weight"
fi
exit 0
