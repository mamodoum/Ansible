#!/usr/bin/env python
#-*- coding: utf-8 -*- 

############################################################################
# Script permettant de supprimer les sauts dans l'output "show interface"
# du Nexus 5672UP - 6001 - 5624Q - 56128P
############################################################################

import sys
import re

# RegEx afin de trouver les patterns correspondant
pattern1 = r"Ethernet*[0-9][0-9][0-9]" 
pattern2 = r" Dedicated Interface"

file_parsed = open((sys.argv[1]+'_2'), "w")

with open((sys.argv[1]), 'r') as file_brut: #prend en entrée le 2e argument de la commande python (le nom du fichier)
	for line in file_brut.readlines():
		if re.match(pattern2,line) or re.match(pattern1,line) : #recherche le pattern ligne par ligne
			#print (line)
			file_parsed.write(line[:-1]) #supprime les 2 derniers caractères --> \n (le saut de ligne)
		else:
			file_parsed.write(line)



#newfile = open("result.txt", "w")
#with open('asset_5672_court.txt', 'r') as monfichier:
#	for line in monfichier.readlines():
#		if re.search('\S', line): # match any non-whitespace character --> surprimme les sauts de lignes
#			newfile.write(line)