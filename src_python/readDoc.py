#! python3

import docx
import os


def getText(fullFileName):
	filename, fileext = os.path.splitext(fullFileName)
	if fileext == ".docx" :
		return getTextFromDocX(fullFileName)
	if fileext == ".txt" :
		return getTextFromTxt(fullFileName)
	return ""

def getTextFromDocX(filename):
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)

def getTextFromTxt(filename):
	txt = open(filename, 'r')
	fullText = []
	for para in txt:
		fullText.append(para)
	return '\n'.join(fullText)
