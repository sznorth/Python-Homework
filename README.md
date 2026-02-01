# Python Homework 
DevOps beadandó feladat weboldal címkészlet feldolgozásról.

### Függőségek

 - **Python** : python 3
 - **Python | requests** : py requests modul
 - **Python | BeautifulSoup4** : py BeautifulSoup4 modul
 - **Python | io** : py io modul (UTF8 kódolás)

## Futtatás
Futtatáshoz használd a main.py -t.

## Felépítés
A script az OOP elvek figyelembe vételével készült.

- **main.py**
A script indítását végzi, a szükséges változókat definiálja és metódusokat hív meg.
 
Változók:
*url*       : a feltérképezendő weboldal címe
*level*     : tartalom elem szint filter definiálása
*filename*  : tartalom mentéshez file elnevezés
*response*  : visszakapott érték tárolása

- **loader.py**
A különböző műveletek és a *Title* osztály definiálása.
 
Title osztály: egy tulajdonságot tartalmaz ez a text
Metódusok:
*webmapper*     : letölti és html alapon parsol-ja a tartalmat
*printFiltered* : letöltött tartalmat filterezi és kiírja kimenetre
*fileWrite*     : letöltött tartalmat filterezi és kiírja egy file-ba

## License
MIT

## Author Information
Szabó Bence István