# Парсер вакансий с hh.ru <img src="https://i.hh.ru/logos/svg/hh.ru__min_.svg" height="32"/> и trudvsem.ru

### release
[![Windows](https://img.shields.io/badge/-Windows_x64-blue.svg?style=for-the-badge&logo=windows)](https://github.com/extybr/parser-vacancies-Headhunter/releases/download/v1.0.0/windows_x64_hh-v1.0.0.zip)
[![Unix](https://img.shields.io/badge/-Linux-red.svg?style=for-the-badge&logo=linux)](https://github.com/extybr/parser-vacancies-Headhunter/releases/download/v1.0.0/linux_install.sh)
##
  <img src="img/preview.jpg" height="400">
 
### Windows:
#### pyinstaller
     pyinstaller main.py -F -w --i=img/favicon.ico
#### nuitka
     python -m nuitka --windows-disable-console --onefile --follow-imports --enable-plugin=pyqt5 --windows-icon-from-ico=img/favicon.ico main.py
