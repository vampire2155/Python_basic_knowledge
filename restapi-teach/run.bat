cd /d %~dp0
set startDir=%cd%
cd "%startDir%\backend"
:: linux ÏÂµÄÆô¶¯ÃüÁî:nohup python3 project/cherrypy_startup.py  /dev/null 2> /dev/null &

python project/cherrypy_startup.py
pause

 
 

