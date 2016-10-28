#!/usr/bin/python

import sys
import filecmp
import os
from stat import *

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv);

fa = open(sys.argv[1], 'r')
listA = []
minSize = 4 #4 Kilobytes

for lineA in fa:
	tokens = lineA.split("\t")
	tokens[0] = int(tokens[0])
	if tokens[0] > minSize :
		if tokens[1].find(".DS_") < 0 :
			tokens[1] = tokens[1].replace("\n","")
			mode = os.stat(tokens[1])[ST_MODE]
        		if not S_ISDIR(mode):
				listA.append(tokens)
fa.close()

listA = sorted(listA,key=lambda a: a[0], reverse=True)

fb = open(sys.argv[2], 'r')
listB = []

for lineB in fb:
	tokens = lineB.split("\t")
	tokens[0] = int(tokens[0])
	if tokens[0] > minSize :
		if tokens[1].find(".DS_") < 0 :
			tokens[1] = tokens[1].replace("\n","")
			mode = os.stat(tokens[1])[ST_MODE]
        		if not S_ISDIR(mode) :
				listB.append(tokens)
fb.close()

listB = sorted(listB,key=lambda b: b[0], reverse=True)

fo = open(sys.argv[3], 'w')

#Compare all the files and folders of A agains B
print "   Step 2.1/2: Matching file sizes"
candidates = []
lngB = len(listB)
indexB = 0
indexC = 0
print listB
for lineA in listA :
	if indexB < lngB :
		print lineA
		b = listB[indexB]
		while lineA[0] < b[0] and indexB < lngB - 1 :
			indexB += 1
			if indexC < lngB :
				b = listB[indexB]
		indexC = indexB
		while lineA[0] == b[0]  and indexC < lngB :
			candidates.append((lineA[0], lineA[1], b[1]))
			indexC += 1
			if indexC < lngB :
				b = listB[indexC]
	else:
		break

print "   Done"

#Now we can save this and use a file comparator to know if they are really the same
print "   Step 2.3/2: Matching the content of the probable candidates"
sum = 0
count = 0
print candidates
for files in candidates:
	if filecmp.cmp(files[1],files[2]): 
		fo.write((str(files[0])+"\t"+files[1]+"\t"+files[2]+"\n"))
		sum += files[0]
		count += 1
print ("resume: "+str(count)+" files "+str(sum)+" Kb")
fo.close()

print "   Done"

