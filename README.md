# Парсер вакансий с hh.ru <img src="https://i.hh.ru/logos/svg/hh.ru__min_.svg" height="32"/> и trudvsem.ru

## Windows:
### pyinstaller
     pyinstaller main.py -F -w --i=img/favicon.ico
### nuitka
     python -m nuitka --windows-disable-console --onefile --follow-imports --enable-plugin=pyqt5 --windows-icon-from-ico=img/favicon.ico main.py

<img src="img/preview.jpg" height="400">
