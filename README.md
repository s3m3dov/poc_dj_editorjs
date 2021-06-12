# Test: Django & Editor.js Integration #

## Getting Started ##

### Installation ###
```
git clone https://github.com/s3m3dov/dj_editorjs
```

### Before Set-up ###
1. Create PostgreSQL db (because sqlite doesn't support JSONfield)
2. Edit `Databases` settings in 'dj_editorjs/settings.py'

### Python/Django Set-up ###

```
virtualenv .env
```
```
source .env/bin/activate
```
or
```
py -m venv env
```
```
env\Scripts\activate
```

then
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```


## Who do I talk to? ##

* Repo owner or admin
* Other community or team contact
