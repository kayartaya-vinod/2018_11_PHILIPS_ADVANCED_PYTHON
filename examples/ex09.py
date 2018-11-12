'''
Module ex09

Rertieving data from db table
'''

from sqlite3 import connect

def main():
    email = input('Enter email for searching: ')
    cmd = 'select * from contacts where email = ?'
    conn = connect('philips_db.sqlite3')
    cur = conn.cursor()
    cur.execute(cmd, (email,))
    data = cur.fetchone()
    cur.close()
    conn.close()

    print('data contains {} values'.format(len(data)))
    print('type of data is {}'.format(type(data)))
    print(data)

if __name__=='__main__': main()