# big-chungus

## local development

first, activate virtualenv 

on Windows
```
source .venv/Scripts/activate
```

on Unix systems
```
source .venv/bin/activate
```

when adding new dependencies, run
```
pip freeze > requirements.txt
```

at this time, the project has not been deployed or dockerized. You must download the browser driver and place it in your PATH aka /usr/bin or /usr/local/bin or C:\WINDOWS\
in order for selenium library to work. This is temporary!!