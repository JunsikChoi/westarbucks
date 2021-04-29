# WESTARBUCKS

## PURPOSE / WHAT TO LEARN
- Modeling DB of Starbucks Drinks
- Crawling Starbucks Drink Data
- Django DB Initialize
- Simple Django CRUD

## REQUIREMENTS
- Python 3.8
- Django
- Selenium
- MySQL
- Local installed Chrome Web Browser (for selenium)
  
## HOW TO RUN
Setup python 3.8 environment + installed local SQL

### Setup MySQL DB
```mysql
# in mysql shell,
# CREATE MySQL DB
create database WESTARBUCKS character set utf8mb4 collate utf8mb4_general_ci;
```

### Modify my_settings_sample.py
Enter your SQL Username and Password and rename file to my_settings_sample.py
```python
# SAMPLE, change filename to my_settings.py after put in your info.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "WESTARBUCKS",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

SECRET = "somesecretkey"
```

### Setup Python Env & Run with Python
```shell
# in project root
pip install -r requirements.txt
python manage.py migrate
python manage.py crawldata
python manage.py populate_db # You can see that your SQL DB is populated with crawled data!
python manage.py runserver
```

