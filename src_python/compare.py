#!/usr/bin/python

import sys
import filecmp
import os
from stat import *

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv);

fa = open(sys.argv[1], 'r')
listA = []
minSize = 16 #16 Kilobytes
if len(sys.argv) > 6 :
	minSize = int(sys.argv[6])

print "Considering files of min: ", minSize, " kb"
folderA = sys.argv[4];
for lineA in fa :
	tokens = lineA.split("\t")
	tokens[0] = int(tokens[0])
	if tokens[0] > minSize :
		tokens[1] = tokens[1].replace(folderA, "").replace("\n","")
		listA.append(tokens)
	else :
		break

print "Folder A: ",folderA, len(listA)
fa.close()

fb = open(sys.argv[2], 'r')
listB = []
folderB = sys.argv[5];
for lineB in fb:
	tokens = lineB.split("\t")
	tokens[0] = int(tokens[0])
	if tokens[0] > minSize :
		tokens[1] = tokens[1].replace(folderB, "").replace("\n","")
		listB.append(tokens)
	else :
		break

print "Folder B: ",folderB, len(listB)
fb.close()

#Compare all the files of A against B
print "   Step 2.1/2: Matching file sizes"
lngA = len(listA)
lngB = len(listB)
indexA = 0
indexB = 0
indexC = 0
nSteps = 100
deltaIndex = lngA / nSteps;
nextReport = deltaIndex;
sum = 0
count = 0
fo = open(sys.argv[3], 'w')

for lineA in listA :
	indexA += 1
	if indexA  > nextReport :
		print indexA, "/", lngA, "current files sizes:", lineA[0]," kb (repeated files: "+str(count)+" space in disk: "+str(sum)+" kb)" 
		nextReport += deltaIndex
	if indexB < lngB :
		b = listB[indexB]
		while lineA[0] < b[0] and indexB < lngB - 1 :
			indexB += 1
			if indexC < lngB :
				b = listB[indexB]
		indexC = indexB
		while lineA[0] == b[0]  and indexC < lngB :
			if filecmp.cmp(folderA+lineA[1], folderB+b[1]) : 
				fo.write((str(lineA[0])+"\t"+lineA[1]+"\t"+b[1]+"\n"))
				sum += lineA[0]
				count += 1
			indexC += 1
			if indexC < lngB :
				b = listB[indexC]
	else:
		break

print ("resume: "+str(count)+" files "+str(sum)+" Kb")
print "   Done"
fo.close()



