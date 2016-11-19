#!/bin/bash

input=$1
output=$2
path=$3

current="$(pwd)"
cd $path
fullPath="$(pwd)"
cd $current

echo "Step 1/1: Adding info column for docx files"
python src_python/addinfo.py $input $output $fullPath

echo "Done"
