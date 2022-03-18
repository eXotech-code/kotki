@echo off
echo Witamy w instalatorze Generatora Kotów
echo Pobieranie Pythona
set "download=bitsadmin /transfer Python-pobieranie /download /priority normal"
%download% https://www.python.org/ftp/python/3.9.11/python-3.9.11-amd64.exe %cd%\python.exe
echo Instalacja interpretera jezyka Python
.\python.exe /quiet PrependPath=1 Include_test=0 InstallLauncherAllUsers=0
SET PIP="%LocalAppData%\Programs\Python39\Scripts"
pip install -r required.txt
echo Program zainstalowany. Pierwsze uruchomienie...
.\genealogy.py
PAUSE