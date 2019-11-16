## Client SOAP pour la gestion des étudiants - Système distribué 
Exemple de client SOAP en python permettant la consommation d'un webservice développé en Java dans le cadre du cours de systèmes distribués 

## Installation

Afin d'installer les dépendances nécessaires au fonctionnement de ce projet, il faut utiliser la gestionnaire de paquets de Python : pip 

```bash

pip install -r requirements.txt
```

## Utilisation
Dans un terminal, se placer dans le dossier package gestion_etudiant et lancer le client voulu avec l'url du fichier wsdl
Par exemple, si le service est sur l'url : http://localhost:8585/?wsdl

```bash
cd /chemin/vers/gestion_etudiant
python client_soap_cli.py http://localhost:8585/?wsdl
```
Ce dossier comporte deux script python : client_soap_cli.py pour la gestion d'une liste d'étudiant à partir d'une console, ainsi que client_soap_gui.py pour la gestion d'une liste à partir d'une interface graphique (GUI). Le GUI est réalisé à l'aide du framework PyQT5.

## Licence
Licence GNU GPL 3
https://www.gnu.org/licenses/gpl-3.0.html
