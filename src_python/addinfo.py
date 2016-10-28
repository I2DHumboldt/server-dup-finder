#!/usr/bin/python

import sys
import readDoc
import os
import json

fa = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

listA = []

keywords = ["informe final ", "documento final", "consultoria",  "presupuesto", "contrato", "convenio", "cronograma", "propuesta", "informe"]

typesByExtension = {".png":"image", ".jpg":"image", ".tiff":"image", ".bmp":"image", ".eps":"image", ".svg":"image", ".gif":"image", ".doc":"document", ".docx":"document", ".xls":"table", ".xlsx":"table", ".csv":"table", ".pdf":"document", ".rtf":"document", ".txt": "plain"}

for lineA in fa:
	lineA = lineA.replace("\n","")
	tokens = lineA.split("\t")
	tokens[0] = int(tokens[0])
	
	info = ""
	type = "other"
	filename, fileext = os.path.splitext(tokens[1])
	
	type = typesByExtension.get(fileext);
	if type :
		lineA += "\t"+type
	else :
		lineA += "\tother"

	if fileext == ".docx" or fileext == ".txt" :
		content = readDoc.getText(tokens[1]).lower();
		for key in keywords :
			if content.find(key)>=0 :
				info += key+","
		if info.endswith(",") :
			info = info[:-1]

		lineA += "\t"+info
	print lineA
	fo.write(lineA+"\n");

fa.close()
fo.close()


