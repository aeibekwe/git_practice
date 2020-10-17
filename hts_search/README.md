This directory is for all things coding and related to work...
I have installed django and requests, but still need to install PostgreSQL and pyscopg2(-binary?).  I will save those installations for when I get further into the project.  For now the most critical installation was requests, so i can interface with the HTS with the http protocol.

prerequisites: (1) python3 installed, (2) pip3 installed, (3) pipenv installed, (4) requests installed with pipenv (and once the pipenv shell is activated, requests still needs to be imported [i.e., >>> import requests, see below]).

to start the interactive shell:
(1) cd to the directory where you have the 'main.py' file saved
(2) enter 'pipenv shell'
(3) enter 'python3' (this will start the IDE, where you can play around with the code)
(4) import the following modules:
	- requests
	- from main import URL, HTS_Search