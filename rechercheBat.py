# -*- coding: utf-8 -*-
import fire
import os
import pathlib
import shutil
import pandas
import yaml
import re

class rechercheBat(object):

    def recherche(self, motClef="null"):
        i = 0
        jsonImm = pathlib.Path("liste-des-immeubles-proteges-au-titre-des-monuments-historiques.json")
        dataJSONImm = pandas.read_json(jsonImm)


        pattern = '^.*('+motClef+').*$'
        for data in dataJSONImm.fields:
            if motClef == "null":
                i = i+1
            if motClef != "null":
                result = re.match(pattern, data["tico"])
                if result:
                    i = i+1
                    # if "desc" in data:
                    #     desc = data["desc"]
                    # else:
                    #     desc = "Non définis"

                    # if "coordonnees_ban" in data:
                    #     coordPart1 = data["coordonnees_ban"][0]
                    #     coordPart2 = data["coordonnees_ban"][1]
                    # else:
                    #     coordPart1 = "Non"
                    #     coordPart2 = "définis"

                    # dossierCible = pathlib.Path("export.yml")
                    
                    # if dossierCible.exists():
                    #     print("")
                    # else:
                    #     dataYaml = dict(
                    #         Nom = data["tico"],
                    #         Desc = desc,
                    #         Commune = data["commune"],
                    #         Localisation = dict(
                    #             Latitude = coordPart1,
                    #             Longitude = coordPart2
                    #         )
                    #     )    
                    #     with open('export.yml', 'w') as outfile:
                    #         yaml.dump(dataYaml, outfile, default_flow_style=False, sort_keys=False, allow_unicode=True)

        if motClef == "null":
            return "Il y a %s monument(s) dans la liste" % i
        else: 
            return "Il y a %s monument(s) dans la liste correspondant à votre mot clef" % i


if __name__ == '__main__':

    rechercheBat = rechercheBat().recherche
    fire.Fire(rechercheBat)