#-*- coding: utf-8 -*-
__author__ = 'jsm'
import xml.etree.ElementTree as ElementTree
import os
import re
from unidecode import unidecode
import pandas as pd

# XML con la lista de candidatos descargado del BOE
# http://www.boe.es/diario_boe/xml.php?id=BOE-A-2014-4577
tree = ElementTree.parse(os.path.join('data', 'candidatos.xml'))
ps = tree.findall("texto/p")

numbers = [str(i) for i in range(10)]

candidatos = []

candidatura = 0
partido = ""
siglas = ""
orden = 0
suplente = False
nombre1 = ""
nombre_completo = ""

b_nombre = False
b_candidatos = False
b_suplentes = False

for p in ps:
    t = p.text.strip()
    if b_candidatos or b_suplentes:
        if (not t.startswith("Suplentes")) and (t[0] in numbers):
            c = t.split(".")
            orden = int(c[0])
            nombre_completo = ".".join(c[1:])
            nombre1 = unidecode(nombre_completo.strip().split(" ")[0])
            #print candidatura, partido, orden, nombre_completo, suplente, nombre1
            candidatos.append({"candidatura": candidatura,
                               "partido": partido,
                               "siglas": siglas,
                               "suplente": suplente,
                               "numero": orden,
                               "nombre": nombre1,
                               "nombre_completo": nombre_completo})
        elif t.startswith("Suplentes"):
            pass
        else:
            b_candidatos = False
            b_suplentes = False

    if b_nombre:
        partido = t
        # Siglas
        alt = re.findall("(?<= )\((.*)\).*", t)
        # Si no hay siglas entre parentesis se toman las dos últimas palabras
        if alt == []:
            alt = re.findall("(\w+\s\w+)$", t)
        siglas = unidecode(alt[0])
        b_candidatos = True
        b_nombre = False

    if t.startswith(u"CANDIDATURA NÚMERO"):
        candidatura = int(t[18:])
        suplente = False
        b_nombre = True
        b_suplentes = False

    if t.startswith("Suplentes") and b_candidatos:
        suplente = True
        b_candidatos = False
        b_suplentes = True

data = pd.DataFrame(candidatos)

save = True
if save:
    data.to_csv(os.path.join('data', 'candidatos.csv'), encoding="utf-8")
    store = pd.HDFStore(os.path.join('data', 'candidatos.h5'))
    store["data_init"] = data
    store.close()
