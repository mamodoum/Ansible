#!/usr/bin/python
# -*- coding:utf-8 -*-

### Pour lancer le script, utiliser la commande suivante:
##  python3.5 <fichier>.py  ##

import time
start = time.time()

import getpass
import paramiko
from openpyxl import Workbook
from openpyxl import load_workbook
import csv

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

print('\n')

#On commence par ouvrir le fichier input.csv contenant les IP/hostnames en lecture
#filename = 'input.csv'
#filecsv = open(filename, 'r')

#On commence par ouvrir le fichier ExportPolluxCiscoActiveHSG.XLSX contenant les UsualNames en lecture
filexlsx = load_workbook(filename = "ExportPolluxCiscoActiveHSG.XLSX")
xlsx = filexlsx['exportLight20180525_111421']

#Il faut ensuite saisir les identifiants permettant de se connecter aux équipements
username = input("Saisissez votre identifiant: ")
password = getpass.getpass("Saisissez votre mot de passe: ")
print ('\n')

#On récupère ensuite les UsualNames se trouvant dans la première colonne du fichier csv (result[0])
#for row in filecsv:
#	result = row.split(";")
#	tab_equipements.append(result[0])

#On récupère ensuite les UsualNames se trouvant dans la deuxieme colonne du fichier xlsx
#Ces valeurs sont stockés dans un dictionnaire qui lui meme sera rajouté à un tableau
#Cela permet d'acceder plus facilement aux données qui nous interessent
#Le matricule (asset_id) est récupéré a des fins de tests.
tab_equipements = []
for x in xlsx.rows:
	if x[1].value != None:
		dictionnaire = {
			'UsualName' : x[1].value,
			'Matricule' : x[0].value
		}
		tab_equipements.append(dictionnaire)


#On retire les entetes de colonnes pour ne conserver que les UsualNames
tab_equipements.remove(tab_equipements[0])


#Ces deux fichiers serviront a differencier les hosts auxquels on arrive a se connecter et 
#ceux auquels on n'arrive pas a se connecter
#Attention, ouverture des fichiers en écriture et écrasement des données y figurant préalablement!!!
f1 = open('ssh_ok.csv', 'w')
f2 = open('ssh_non_ok.csv', 'w')

#Le module paramiko permet d'utiliser ssh v2 pour se connecter aux equipements
#On parcourt donc le tableau contenant l'UsualName des équipements
#On commence par créer un client ssh à qui, une fois qu'on a fourni l'UsualName de l'equipement concerné, le username,
#et le password, pourra initier la connexion ssh indépendamment du systeme d'exploitation du host ciblé.
for equipement in tab_equipements:
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
	client.load_system_host_keys()
	try:
		client.connect(equipement['UsualName'], username=username, password=password, look_for_keys=False, allow_agent=False)
		print('Connexion reussie a '+equipement['UsualName'])
		print ('\n')
		f1.write(equipement['UsualName']+'\n')
	except:
		print('Connexion non reussie a '+equipement['UsualName'])
		print ('\n')
		f2.write(equipement['UsualName']+'\n')

	f2.write(equipement['UsualName']+'\n')

#Le module paramiko permet d'utiliser ssh v2 pour se connecter aux equipements
#for equipement in tab_equipements:
#	client = paramiko.SSHClient()
#	client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
#	client.load_system_host_keys()
#	try:
#		client.connect(equipement, username=username, password=password, look_for_keys=False, allow_agent=False)
#		print('Connexion reussie a '+equipement)
#		print ('\n')
#		f1.write(equipement+'\n')
#	except:
#		print('Connexion non reussie a '+equipement)
#		print ('\n')
#		f2.write(equipement+'\n')

#On s'assure de fermer les fichiers ssh_ok.csv et ssh_non_ok.csv
f1.close()
f2.close()

#filecsv.close()

print("\n######################################")
print("Script .... ....Completed")
print("######################################")
print ('\nIt tooks', int((time.time()-start)/60), 'minutes',  float((time.time()-start)%60), 'seconds.')
print ("\n")