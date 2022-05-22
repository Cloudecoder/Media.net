#!/bin/bash

read -p "Enter DIR path: " path
count=$(ls -l $path | wc -l )

echo $path "No of Files-" $count 

lines=$(cat $i | wc -l)

for i in $path/*; do echo $i "-No of lines in the file:" $lines; done
