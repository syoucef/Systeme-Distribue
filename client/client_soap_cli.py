#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client_soap.py
#  
#  Copyright 2019 KADI Amine amine.kadi2@etu.univ-lorraine.fr
#                 VASSE Joseph 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  

from zeep import Client
import sys
import time


# =======================
#   FUNCTIONS AFFICHAGE
# =======================

def header(message) :
    ''' Fonction header : sert à afficher délimiter dans le terminal et 
    séparer les informations.
    Prend en argument le message à afficher'''
    print('-'*60)
    print(message)
    print('-'*60)

# =======================
#   FUNCTIONS MENU
# =======================

# Fin programme
def exit():
    print("Fin du programme")
    sys.exit()

# Menu principal
def main_menu():
    header("Gestion d'une liste d'étudiants")
    choice='0'
    while choice =='0':
        print("Choisissez une des 5 options")
        print("1 - Ajouter")
        print("2 - Modifier ")
        print("3 - Supprimer")
        print("4 - Afficher tout")
        print("9 - Pour sortir du programme")

        choice = input ("Faites un choix: ")

        if choice == "9":
            exit()
        elif choice == "4":
            afficher()
        elif choice == "3":
           supprimer()
        elif choice == "2":
            modifier()
        elif choice == "1":
            ajouter()
        else:
            print("Je n'ai pas compris, entrez un chiffre entre 1 et 9")
            retour()

# Retour menu principal
def retour():
    input("Appuyez sur entrez pour revenir au menu principal")
    print('Retour au menu principal')
    time.sleep(0.5)
    main_menu()

# =======================
#  FUNCTIONS TRAITEMENT
# =======================
def afficher():
    header("Affichage de tous les étudiants")
    dico = client.service.afficherToutEtu()
    for i in range(len(dico)):
        print('Etudiant n°'+ str(i+1) 
        + ' - Prenom : ' + dico[i].prenom 
        + ' / Nom : ' +  dico[i].nom + ' \n')
    retour()

def ajouter():
    header("Ajout d'un étudiant dans la liste")
    prenom = input("Entrez le prenom de l'étudiant à ajouter à la liste : ")
    nom = input("Entrez le nom de l'étudiant à ajouter à la liste : ")
    client.service.ajouterEtu(prenom, nom)
    print('Etudiant ajouté')
    retour()

def modifier():
    header("Modification d'un étudiant de la liste")
    old_prenom = input("Entrez le prenom de l'étudiant à "
    +"modifier dans la liste : ")
    old_nom = input("Entrez le nom de l'étudiant à "
    +"modifier dans la liste : ")
    new_prenom = input("Entrez le nouveau prenom de l'étudiant : ")
    new_nom = input("Entrez le nouveau nom de l'étudiant : ")
    client.service.modifierEtu(old_prenom, old_nom, new_prenom, new_nom)
    print('Etudiant modifié')
    retour()

def supprimer():
    header("Suppression d'un étudiant de la liste")
    prenom = input("Entrez le prenom de l'étudiant à "
    +"supprimer dans la liste : ")
    nom = input("Entrez le nom de l'étudiant à supprimer dans la liste : ")
    client.service.supprimerEtu(prenom, nom)
    print('Etudiant supprimé')
    retour()


# =======================
#     CONSTANTES
# =======================
WSDL = sys.argv[1]



# =======================
#          MAIN
# =======================
if __name__ == "__main__":
    client = Client(wsdl = WSDL)
    main_menu()