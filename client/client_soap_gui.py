#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client_soap_gui.py
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


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from zeep import Client
import sys





class Ui_Liste_Etudiants(object):

# =======================
#   FUNCTIONS WEBMETHOD
# =======================    

    def afficherUI(self, Liste_Etudiants):
        dico = client.service.afficherToutEtu()
        chaine =''
        for i in range(len(dico)):
            chaine = chaine+('Etudiant n°'+ str(i+1) 
            + ' - Prenom : ' + dico[i].prenom 
            + ' / Nom : ' +  dico[i].nom + ' \n')
        
        self.label_affich.setText(chaine)

    def modifierUI(self, Liste_Etudiants):
        ancien_prenom = self.lineEdit_Oldprenom.text()
        ancien_nom = self.lineEdit_Oldnom.text()
        nouveau_prenom = self.lineEdit_Newprenom.text()
        nouveau_nom = self.lineEdit_Newnom.text()

        client.service.modifierEtu(ancien_prenom,ancien_nom,nouveau_prenom,nouveau_nom)
        self.label_affich.setText("Etudiant modifié")

        self.lineEdit_prenom_suppr.setText("")
        self.lineEdit_nom_suppr.setText("")

    def supprimerUI(self, Liste_Etudiants):
        prenom =''
        prenom = self.lineEdit_prenom_suppr.text()
        nom = self.lineEdit_nom_suppr.text()

        print(client.service.supprimerEtu(prenom,nom))

        self.lineEdit_prenom_suppr.setText("")
        self.lineEdit_nom_suppr.setText("")

        self.label_affich.setText("etudiant supprimé")
        return()

    def ajouterUI(self, Liste_Etudiants):
        prenom=self.lineEdit_prenom_ajout.text()
        nom = self.lineEdit_nom_ajout.text()

        client.service.ajouterEtu(prenom,nom)

        self.lineEdit_prenom_ajout.setText(" ")
        self.lineEdit_nom_ajout.setText(" ")

        self.label_affich.setText("etudiant ajouté")


# =======================
#   FUNCTIONS QT
# =======================

    def setupUi(self, Liste_Etudiants):
        Liste_Etudiants.setObjectName("Liste_Etudiants")
        Liste_Etudiants.resize(1250, 579)
        self.centralwidget = QtWidgets.QWidget(Liste_Etudiants)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(10, 70, 334, 21))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.box_affichage = QtWidgets.QGroupBox(self.centralwidget)
        self.box_affichage.setGeometry(QtCore.QRect(10, 190, 681, 231))
        self.box_affichage.setObjectName("box_affichage")
        self.pushButton_affich = QtWidgets.QPushButton(self.box_affichage)
        self.pushButton_affich.setGeometry(QtCore.QRect(420, 30, 201, 31))
        self.pushButton_affich.setObjectName("pushButton_affich")
        self.label_affich = QtWidgets.QLabel(self.box_affichage)
        self.label_affich.setGeometry(QtCore.QRect(0, 30, 411, 111))
        self.label_affich.setObjectName("")
        self.Box_ajout = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_ajout.setGeometry(QtCore.QRect(10, 0, 411, 61))
        self.Box_ajout.setObjectName("Box_ajout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.Box_ajout)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.splitter = QtWidgets.QSplitter(self.Box_ajout)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_nom_ajout = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_nom_ajout.setObjectName("label_nom_ajout")
        self.horizontalLayout_3.addWidget(self.label_nom_ajout)
        self.lineEdit_nom_ajout = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_nom_ajout.setObjectName("lineEdit_nom_ajout")
        self.horizontalLayout_3.addWidget(self.lineEdit_nom_ajout)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_prenom_ajout = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_prenom_ajout.setObjectName("label_prenom_ajout")
        self.horizontalLayout_4.addWidget(self.label_prenom_ajout)
        self.lineEdit_prenom_ajout = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_prenom_ajout.setObjectName("lineEdit_prenom_ajout")
        self.horizontalLayout_4.addWidget(self.lineEdit_prenom_ajout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bouton_ajout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Bouton_ajout.setObjectName("Bouton_ajout")
        self.horizontalLayout.addWidget(self.Bouton_ajout)
        self.horizontalLayout_13.addWidget(self.splitter)
        self.Box_suppression = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_suppression.setGeometry(QtCore.QRect(10, 50, 401, 61))
        self.Box_suppression.setObjectName("Box_suppression")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Box_suppression)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.splitter_5 = QtWidgets.QSplitter(self.Box_suppression)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.splitter_5)
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_nom_suppr = QtWidgets.QLabel(self.horizontalLayoutWidget_18)
        self.label_nom_suppr.setObjectName("label_nom_suppr")
        self.horizontalLayout_18.addWidget(self.label_nom_suppr)
        self.lineEdit_nom_suppr = QtWidgets.QLineEdit(self.horizontalLayoutWidget_18)
        self.lineEdit_nom_suppr.setObjectName("lineEdit_nom_suppr")
        self.horizontalLayout_18.addWidget(self.lineEdit_nom_suppr)
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.splitter_5)
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_prenom_suppr = QtWidgets.QLabel(self.horizontalLayoutWidget_19)
        self.label_prenom_suppr.setObjectName("label_prenom_suppr")
        self.horizontalLayout_19.addWidget(self.label_prenom_suppr)
        self.lineEdit_prenom_suppr = QtWidgets.QLineEdit(self.horizontalLayoutWidget_19)
        self.lineEdit_prenom_suppr.setObjectName("lineEdit_prenom_suppr")
        self.horizontalLayout_19.addWidget(self.lineEdit_prenom_suppr)
        self.horizontalLayoutWidget_20 = QtWidgets.QWidget(self.splitter_5)
        self.horizontalLayoutWidget_20.setObjectName("horizontalLayoutWidget_20")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.Bouton_suppr = QtWidgets.QPushButton(self.horizontalLayoutWidget_20)
        self.Bouton_suppr.setObjectName("Bouton_suppr")
        self.horizontalLayout_20.addWidget(self.Bouton_suppr)
        self.horizontalLayout_12.addWidget(self.splitter_5)
        self.box_modification = QtWidgets.QGroupBox(self.centralwidget)
        self.box_modification.setGeometry(QtCore.QRect(10, 100, 891, 81))
        self.box_modification.setObjectName("box_modification")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.box_modification)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.splitter_2 = QtWidgets.QSplitter(self.box_modification)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_OldNom = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_OldNom.setObjectName("label_OldNom")
        self.horizontalLayout_11.addWidget(self.label_OldNom)
        self.lineEdit_Oldnom = QtWidgets.QLineEdit(self.horizontalLayoutWidget_11)
        self.lineEdit_Oldnom.setObjectName("lineEdit_Oldnom")
        self.horizontalLayout_11.addWidget(self.lineEdit_Oldnom)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_Oldprenom = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_Oldprenom.setObjectName("label_Oldprenom")
        self.horizontalLayout_7.addWidget(self.label_Oldprenom)
        self.lineEdit_Oldprenom = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_Oldprenom.setObjectName("lineEdit_Oldprenom")
        self.horizontalLayout_7.addWidget(self.lineEdit_Oldprenom)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Newnom = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_Newnom.setObjectName("label_Newnom")
        self.horizontalLayout_10.addWidget(self.label_Newnom)
        self.lineEdit_Newnom = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_Newnom.setObjectName("lineEdit_Newnom")
        self.horizontalLayout_10.addWidget(self.lineEdit_Newnom)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_Newprenom = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_Newprenom.setObjectName("label_Newprenom")
        self.horizontalLayout_8.addWidget(self.label_Newprenom)
        self.lineEdit_Newprenom = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_Newprenom.setObjectName("lineEdit_Newprenom")
        self.horizontalLayout_8.addWidget(self.lineEdit_Newprenom)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.splitter_2)
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_Modif = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButton_Modif.setObjectName("pushButton_Modif")
        self.horizontalLayout_9.addWidget(self.pushButton_Modif)
        self.horizontalLayout_14.addWidget(self.splitter_2)
        self.Box_ajout.raise_()
        self.splitter_3.raise_()
        self.box_affichage.raise_()
        self.Box_suppression.raise_()
        self.box_modification.raise_()
        Liste_Etudiants.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Liste_Etudiants)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 25))
        self.menubar.setObjectName("menubar")
        Liste_Etudiants.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Liste_Etudiants)
        self.statusbar.setObjectName("statusbar")
        Liste_Etudiants.setStatusBar(self.statusbar)


        self.Bouton_ajout.clicked.connect(self.ajouterUI)
        self.pushButton_affich.clicked.connect(self.afficherUI)
        self.Bouton_suppr.clicked.connect(self.supprimerUI)
        self.pushButton_Modif.clicked.connect(self.modifierUI)

        self.retranslateUi(Liste_Etudiants)
        QtCore.QMetaObject.connectSlotsByName(Liste_Etudiants)

    def retranslateUi(self, Liste_Etudiants):
        _translate = QtCore.QCoreApplication.translate
        Liste_Etudiants.setWindowTitle(_translate("Liste_Etudiants", "Liste Etudiants"))
        self.box_affichage.setTitle(_translate("Liste_Etudiants", "Affichage des Etudiants."))
        self.pushButton_affich.setText(_translate("Liste_Etudiants", "Afficher les etudiants"))
        self.label_affich.setText(_translate("Liste_Etudiants", "TextLabel"))
        self.Box_ajout.setTitle(_translate("Liste_Etudiants", "Ajouter Etudiant"))
        self.label_nom_ajout.setText(_translate("Liste_Etudiants", "Nom :"))
        self.label_prenom_ajout.setText(_translate("Liste_Etudiants", "Prénom :"))
        self.Bouton_ajout.setText(_translate("Liste_Etudiants", "Ajouter"))
        self.Box_suppression.setTitle(_translate("Liste_Etudiants", "Supprimer Etudiant"))
        self.label_nom_suppr.setText(_translate("Liste_Etudiants", "Nom :"))
        self.label_prenom_suppr.setText(_translate("Liste_Etudiants", "Prénom :"))
        self.Bouton_suppr.setText(_translate("Liste_Etudiants", "Supprimer"))
        self.box_modification.setTitle(_translate("Liste_Etudiants", "Modification Etudiant"))
        self.label_OldNom.setText(_translate("Liste_Etudiants", "Ancien Nom"))
        self.label_Oldprenom.setText(_translate("Liste_Etudiants", "Ancien prénom"))
        self.label_Newnom.setText(_translate("Liste_Etudiants", "Nouveau nom"))
        self.label_Newprenom.setText(_translate("Liste_Etudiants", "Nouveau prénom"))
        self.pushButton_Modif.setText(_translate("Liste_Etudiants", "Modifier"))



# =======================
#     CONSTANTES
# =======================
WSDL = sys.argv[1]



# =======================
#          MAIN
# =======================
if __name__ == "__main__":
    client = Client(wsdl = WSDL)

    app = QtWidgets.QApplication(sys.argv)
    Liste_Etudiants = QtWidgets.QMainWindow()
    ui = Ui_Liste_Etudiants()
    ui.setupUi(Liste_Etudiants)
    Liste_Etudiants.show()
    sys.exit(app.exec_())
