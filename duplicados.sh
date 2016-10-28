#!/bin/bash

A=$1
B=$2
output=$3

echo "Step 1/2: listing files..."

du -ak $A > tmpfiles/lsA.txt
du -ak $B > tmpfiles/lsB.txt

echo "Done"

echo "Step 2/2: Finding matches"

python src_python/compare.py tmpfiles/lsA.txt tmpfiles/lsB.txt $output
#python src_python/addinfo.py $output $output."info"

echo "Done"
