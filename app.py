# Patching
from flask import Flask, render_template, request
# Denne bruges til at, hente SQL
import psycopg2
import requests
import pandas as pd

# Create a new app
app = Flask(__name__)

#   Database initialization
# Connect to database
try:
    conn = psycopg2.connect("dbname='bank' user='postgres' host='localhost' password='5555'")
    print(' * Succesfully connected to database')
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

### Create List 
cur.execute("""SELECT * FROM curr """)
rows = cur.fetchall()

list = [row[0] for row in rows]
rate = [row[2] for row in rows]

# Define Functions

def select_rate(base):
    cur = conn.cursor()
    sql = """
    SELECT rate
    FROM curr
    WHERE code = %s
    """
    cur.execute(sql, (base,))
    rate = cur.fetchone() if cur.rowcount > 0 else None;
    cur.close()
    return rate[0]
               
        
def find_amout(base,end,amount):
    base = select_rate(base)
    end = select_rate(end)

    c = base * float(amount)
    i = c * (1/end)
    return i

# Define Function        

@app.route('/',methods = ['POST','GET'])
def index():
    res_amount = 0.0
    currencies = list # rows
    if request.method == 'POST':
        base = request.form.get("base")
        end  = request.form.get('end')
        amount = request.form.get('amount')
        res_amount = find_amout(base, end, amount)
        
    return render_template('index.html', currencies = currencies,output=res_amount)

@app.route("/about",)
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.debug = True
    app.run()
    
    