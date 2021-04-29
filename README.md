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

```mysql
# in mysql shell,
# CREATE MySQL DB
create database WESTARBUCKS character set utf8mb4 collate utf8mb4_general_ci;
```

```shell
# in project root
pip install -r requirements.txt
python manage.py migrate
python manage.py crawldata
python manage.py populate_db
python manage.py runserver
```