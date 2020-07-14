cd /d %~dp0
set startDir=%cd%
cd "%startDir%\backend"
nohup python3 project/cherrypy_startup.py  /dev/null 2> /dev/null &

pause

 
 

