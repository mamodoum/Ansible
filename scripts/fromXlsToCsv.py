#!/usr/bin/python
# -*- coding:utf-8 -*-

### Pour lancer le script, utiliser la commande suivante:
##  python3.5 <fichier>.py  ##

import time
start = time.time()

import xlrd
import unicodecsv
import csv
import os

# Le script convertit un fichier Excel en fichier CSV.
# Si le fichier Excel contient plusieurs feuilles de calcul, seule la première feuille de calcul est convertie.
# Utilisation de la librairie unicodecsv, donc il va gérer les caractères Unicode.
# Utilisation d'une version récente de xlrd, donc il devrait aussi bien gérer les anciens .xls que les nouveaux .xlsx, xlsm, etc.

print('\n')
print (' ________________________________________________')
print ('|        ____________    ____________            |')
print ('|        |               |                       |')
print ('|        |               |                       |')
print ('|        |____________   |   _________           |')
print ('|                    |   |           |           |')
print ('|                    |   |           |           |')
print ('|                    |   |           |           |')
print ('|        _____________   _____________           |')
print ('|                                                |')
print (' ________________________________________________')   
print('\n')

print("Script is running.")
print("\n")

#Saisir le nom du fichier avec l'extension, exemple : monfichierexcel.xlsx ou monfichierexcel.xls ou monfichierexcel.xls etc...
xls_filename = input("Saisissez le nom du fichier Excel (xls ou xlsx) : ")

#Le try - except permet de gérer les erreurs de saisie.
#Dans le try, on récupère l'extension du fichier et on la supprime du nom du fichier afin de pouvoir
#rajouter la nouvelle extension qui est "csv", puis on ouvre le fichier excel
#Si l'utilisateur saisit le nom d'un fichier qui n'existe pas, le script affiche un message explicite
#et le programme s'arrête automatiquement.
try:
	_, extension = os.path.splitext(xls_filename)
	csv_filename = xls_filename.replace(extension,"")+".csv"
	workbook = xlrd.open_workbook(xls_filename)
	sheet = workbook.sheet_by_index(0)
except:
		print("Impossible d'ouvrir le fichier: "+xls_filename)
		print("Veuillez relancer le programme et saisir un nom de fichier existant.")
		print ("Exit..")
		print ("\n")
		exit()

#Ouverture du fichier csv
#Le délimiteur sera un point virgule et il y aura des quotes autour de chaque élément 
csv_file = open(csv_filename,"wb")
csv_out = unicodecsv.writer(csv_file, encoding='utf-8', delimiter=',', quoting=csv.QUOTE_ALL)

print("\n")
print("Conversion in progress en cours..")
print("\n")

#Récupération des éléments du fichier excel et insertion de ces éléments dans le fichier csv
for row_number in range(sheet.nrows):
    csv_out.writerow(sheet.row_values(row_number))

#Fermeture du fichier csv
csv_file.close()

#Fin du script
print("\n######################################")
print("Script .... ....Completed")
print("######################################")
print ('\nIt tooks', int((time.time()-start)/60), 'minutes',  float((time.time()-start)%60), 'seconds.')
print ("\n")