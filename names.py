#-*- coding: utf-8 -*-
__author__ = 'jsm'
import pandas as pd
import numpy as np
import os
import urllib2
import pickle

store = pd.HDFStore(os.path.join('data', 'candidatos.h5'))
data = store["data_init"]
store.close()

# Load gender of the names from internet
get_gender = False
if get_gender:
    name_api = "http://api.onomatic.com/onomastics/api/gendre/{}/es"

    print data.columns

    out = []
    for n in data["nombre"].unique():
        response = urllib2.urlopen(name_api.format(n))
        o = float(response.read())
        print n, n, o
        out.append({"name": n,
                    "name_decoded": n,
                    "gender": o})
        pickle.dump(out, open(os.path.join('data', 'names.pckl'), "w"))

process_gender = True
if process_gender:
    out = pickle.load(open(os.path.join('data', 'names.pckl'), "r"))

    manual_names = {u"Adargoma": -1.0,
                    u"Attissa": 1.0,
                    u"Maixabel": 1.0,
                    u"M.ª": 1.0,
                    u"Inaciu": -1.0,
                    u"Lexuri": 1.0,
                    u"Chusé": -1.0,
                    u"Florisabel": 1.0,
                    u"Mazaly": 1.0,
                    u"Xesús": -1.0,
                    u"Mikeldi": -1.0,
                    u"Arturu": -1.0,
                    u"Aminetou": 1.0,
                    u"Ikoitz": -1.0,
                    u"Cariño": 1.0,
                    u"Izascun": 1.0,
                    u"Lloic": -1.0,
                    u"Eródica": 1.0,
                    u"Naxalli": 1.0,
                    u"Moraia": 1.0,
                    u"Asunción": 1.0,
                    u"Estel": 1.0,
                    u"Reyes": 1.0,
                    u"Martí": -1.0,
                    u"Joan": -1.0,
                    }

    # Replace undefined or wrong gender with the manual gender
    for n in out:
        if n["name"] in manual_names.keys():
            n["gender"] = manual_names[n["name"]]

    names = pd.DataFrame(out, columns=[u"name", u"name_decoded", u"gender"])

    names["gender"] = np.sign(names["gender"])
    #print names
    names.to_csv(os.path.join('data', 'names.csv'), encoding="utf-8")

    print len(data)
    data2 = data.reset_index().merge(names[[u"name_decoded", u"gender"]], how="left",
        left_on="nombre", right_on=u"name_decoded").set_index('index').sort().drop_duplicates()
    del data2[u"name_decoded"]

    #print data2[["nombre", "gender"]]
    data2.to_csv(os.path.join('data', 'data.csv'), encoding="utf-8")
    store = pd.HDFStore(os.path.join('data', 'candidatos.h5'))
    store["data"] = data2
    store.close()
