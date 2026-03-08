# Python Homework
DevOps beadandó feladat weboldal címkészlet feldolgozásról.

### Függőségek

 - **Python** : python 3
 - **Python | requests** : py requests modul
 - **Python | BeautifulSoup4** : py BeautifulSoup4 modul
 - **Python | io** : py io modul (UTF8 kódolás)

## Futtatás
1. Győződj meg róla, hogy telepítve van a Python 3.8+.
2. Hozz létre és aktiválj egy virtuális környezetet (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

3. Telepítsd a futtatáshoz szükséges csomagokat:
```powershell
pip install -r requirements.txt
```

4. Futtasd a szkriptet:
```powershell
python main.py
```

## Felépítés
A script az OOP elveket figyelembe véve készült.

- **main.py**
A script indítását végzi, a szükséges változókat definiálja és metódusokat hív meg.
**Változók**:
-- *url*       : a feltérképezendő weboldal címe
-- *level*     : tartalom elem szint filter definiálása
-- *filename*  : tartalom mentéshez file elnevezés
-- *response*  : visszakapott érték tárolása

- **loader.py**
A különböző műveletek és a *Title* osztály definiálása.
**Title osztály**: egy tulajdonságot tartalmaz ez a text
**Metódusok**:
-- *webmapper*     : letölti és html alapon parsol-ja a tartalmat
-- *printFiltered* : letöltött tartalmat filterezi és kiírja kimenetre
-- *fileWrite*     : letöltött tartalmat filterezi és kiírja egy file-ba

## License
MIT

## Author Information
Szabó Bence István
