Gender of the Spanish candidates for the 2014 EU Elections
==========================================================

Code to analyse the gender of the Spanish candidates for the EU Elections.

Loading and pre-processing of the data
--------------------------------------

The data of the candidates is read from ```candidatos.xml``` which was
downloaded from the BOE
([http://www.boe.es/diario_boe/xml.php?id=BOE-A-2014-4577]). This is done with
```parse_list.py```.

The names of the candidates are detected and the gender is determined using a
web service ([http://namesorts.com/api/]). In the cases were the gender cannot
be determined by the name or the match is wrong the gender is manually
corrected. This part is done with ```names.py```.

The final data is stored in the ```data``` directory. The file HDF5
```candidatos.h5``` contains a table called ```data``` with the data of the
candidates. This table can be found in ```data.csv``` in csv format.

Part of the code is commented in Spanish.

Analysis of the data
--------------------

The data is analysed and commented using IPython notebooks like
```genero_diputados.ipynb```.

At the moment, the notebooks are writen in Spanish.
