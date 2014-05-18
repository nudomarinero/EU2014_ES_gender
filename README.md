Gender of the Spanish candidates for the 2014 EU Elections
==========================================================

Code to analyse the gender of the Spanish candidates for the EU Elections.

Loading and pre-processing of the data
--------------------------------------

The data of the candidates is read from _candidatos.xml_ which was
downloaded from the [BOE](http://www.boe.es/diario_boe/xml.php?id=BOE-A-2014-4577). 
This is done with _parse\_list.py_.

The names of the candidates are detected and the gender is determined using a
[web service](http://namesorts.com/api/). In the cases were the gender cannot
be determined by the name or the match is wrong the gender is manually
corrected. This part is done with _names.py_.

The final data is stored in the _data_ directory. The HDF5 file
_candidatos.h5_ contains a table called _data_ with the data of the
candidates. This table can be found in _data.csv_ in csv format.

Part of the code is commented in Spanish.

Analysis of the data
--------------------

The data is analysed and commented using IPython notebooks like
_genero\_diputados.ipynb_.

At the moment, the notebooks are writen in Spanish.

Links to the notebooks on the Notebook Viewer:
* [genero_diputados.ipynb](http://nbviewer.ipython.org/github/nudomarinero/EU2014_ES_gender/blob/master/genero_diputados.ipynb)
