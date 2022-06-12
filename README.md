# Currency Converter
## Running the Web-App:

Assumes a working Python 3 installation (with python=python3 and pip=pip3).

(1) Run the code below to install the dependencies.

>$ pip install -r requirements.txt

(2) Database initialization
1. Set the database name in the app.py file.
2. Run first schema.sql, and then schema_ins.sql in your database. If you want to drop, run schema_drop.sql
OBS: In the 'schema_ins.sql' change the directory to the path of the 'curr.csv' file.

(3) Run Web-App
>$ python app.py

## ER-diagram

![alt text](https://github.com/Rasmushoy/currency_converter/blob/main/ER_Currency.png)


# Juni 12, 2022
The converter takes the amount, the base currency and the desired end currency and provides the converted value. 



