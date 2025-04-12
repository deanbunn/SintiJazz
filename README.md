## Sinti Jazz

A Django training project

### Development Environment Commands

Install pip and venv
```bash
sudo apt install python3-pip python3-venv
```
Create Python Virtual Environment
```bash
python3 -m venv DarkVenv
```
Start Virtual Python Environment
```bash
source ./DarkVenv/bin/activate
```
Install Django 
```bash
pip3 install django
```
Update Django
```bash
pip3 install --upgrade django
```
Stop Virtual Python Environment
```bash
deactivate
```

### Django Project Commands

Create Django Project Folder
```bash
mkdir SintiJazz
cd SintiJazz
django-admin startproject sintijazz .
```
Initialize SQLite Database
```bash
python manage.py migrate
```
Run Local Server
```bash
python manage.py runserver
```
Create App Inside Project Folder
```bash
python manage.py startapp sintijazzapp 
```
Open Django Shell Session
```bash
python manage.py shell
```
Make App Migrations
```bash
python manage.py makemigrations sintijazzapp
```

