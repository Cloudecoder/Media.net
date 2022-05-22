#!/bin/bash

read -p "Enter path:" path

for i in $path/* :
    do touch $i/file_name.txt
done

