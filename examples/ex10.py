'''
Module ex10

Fetch all records from db table
'''
from sqlite3 import connect

def main():
    conn = connect('philips_db.sqlite3')

    cur = conn.cursor()
    cur.execute('select * from contacts')
    data = cur.fetchall()
    if len(data) > 0:
        for rec in data:
            print(rec)
    else:
        print('No data found!')

if __name__=='__main__': main()