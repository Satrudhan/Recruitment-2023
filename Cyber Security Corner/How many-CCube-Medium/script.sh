#!/bin/bash
userid=(553 828 723 698)
sum=0
for i in "${userid[@]}"
do 
    value=$(cat users.txt | grep -w "User ID $i =" | cut -d " " -f5)
    sum=$((sum + value))
done

echo "The sum is : $sum"


