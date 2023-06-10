#!/bin/bash
userid=(553 828 723 698)
for i in "${userid[@]}"
do 
    count=$(cat users.txt | grep "$i" | wc -l)
    echo "Count of userid $i: $count"
done
