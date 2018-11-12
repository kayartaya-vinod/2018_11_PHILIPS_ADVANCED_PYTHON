'''
Module ex06

Creating a database table
'''

from sqlite3 import connect

def main():
    cmd = '''create table contacts(
        id integer primary key autoincrement,
        name varchar(50) not null,
        city varchar(50) default 'Bangalore',
        email varchar(100) unique,
        phone varchar(50) unique,
        picture varchar(255)
    )'''

    conn = connect('philips_db.sqlite3')
    c1 = conn.cursor()
    try:
        c1.execute(cmd)
        print('Table "contacts" created!')
    except Exception as e:
        print('There was an error: ')
        print(e)
        
    conn.close()

if __name__=='__main__': main()