from flask import Flask
import psycopg2
import time

time.sleep(4)
app = Flask(__name__)
connection = psycopg2.connect(dbname='postgres', user='postgres',\
                 password='postgres', host='localhost', port=5432)
cursor = connection.cursor()

@app.route('/')
def default():
        cursor.execute('SELECT * FROM test')
        records = cursor.fetchall()
        string = ""
        for i in records:
                string+=str(i)
        string+='\n'
        return string

@app.route('/health')
def health():
    data = {'STATUS': '200', 'CODE': 'SUCCESS'}
    return data, 200

@app.errorhandler(404)
def page_not_found(error):
    return '404 error - "You must to give up, there is no objective truth"!\n', 404

if __name__ == "__main__":
        app.run(debug=True)