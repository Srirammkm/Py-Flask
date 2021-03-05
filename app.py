import os
import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)
mydb = mysql.connector.connect(
  host="54.254.185.134",
  user="root",
  password="root",
  database="MyDB"
)

mycursor = mydb.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        val = [(firstName, lastName)]
        sql = "INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)"
        mycursor.executemany(sql, val)
        mydb.commit()
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
