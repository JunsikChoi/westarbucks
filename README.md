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

```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py crawldata
python manage.py applydata
python manage.py runserver
```