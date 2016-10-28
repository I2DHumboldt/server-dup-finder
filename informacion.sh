#!/bin/bash

input=$1
output=$2

echo "Step 1/1: Adding info column for docx files"
python src_python/addinfo.py $input $output

echo "Done"
