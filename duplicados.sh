#!/bin/bash

#Get the full path of the pahts
current="$(pwd)"
A=$1
B=$2
output=$3
minSize=$4

# I need to do all those stepts to get the absolute paths, because readlink -f is not available in OSX
cd $A
fullA="$(pwd)"
cd $current
cd $B
fullB="$(pwd)"
cd $current

echo "Step 1/2: listing files..."
echo "     working on A"
find $fullA -type f -exec du -ak {} + | sort -n -r > tmpfiles/lsA.txt
echo "     working on B"
find $fullB -type f -exec du -ak {} + | sort -n -r > tmpfiles/lsB.txt
echo "Done"

echo "Step 2/2: Finding matches"

python src_python/compare.py tmpfiles/lsA.txt tmpfiles/lsB.txt $output $fullA $fullB $minSize
#python src_python/addinfo.py $output $output."info"
echo "Done"
