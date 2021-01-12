import fire
import os
import pathlib
import shutil
import pandas
import yaml

def hello(name="World"):
    #On selectionne notre CSV de region/departement
    csv = pathlib.Path("departements-france.csv")
    csvImm = pathlib.Path("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv")
    #On attribut la variable "dossierCible" au dossier renseigner dans la commande 
    dossierCible = pathlib.Path(name)
    
    #Si le dossier cible existe :
    if dossierCible.exists():
        #On demande si l'utilisateur veux le vider
        print ("Le dossier" , name , "existe déjà, voulez vous le vider ?")
        val = input("Oui / Non : ")
        
        #Si oui :
        if val == "Oui":
            #On le supprime lui, et toute l'arboresense en dessosus
            shutil.rmtree(name)
            # et on le recréer
            os.mkdir(name)
        
        #Sinon
        else:
            #On retourne une erreur
            return "Impossible de continuer"
        
    #Si le dossier cible n'existe pas :'pen
    else:
        #On le créer
        os.mkdir(name)
        
    dataCSVRegion = pandas.read_csv(csv, usecols= ['nom_region'])
    dataCSVRegion = dataCSVRegion.drop_duplicates()
    dataCSVDep = pandas.read_csv(csv, usecols= ['nom_departement','nom_region'])
    os.chdir(name)
    
    for data in dataCSVRegion.nom_region:
        os.mkdir(data)
    
    for data in dataCSVDep.iterrows():
        os.chdir(data[1].nom_region)
        os.mkdir(data[1].nom_departement)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
    
    return "Hello %s!" % name

if __name__ == '__main__':
    fire.Fire(hello)