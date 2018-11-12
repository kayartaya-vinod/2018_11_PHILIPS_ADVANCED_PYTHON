'''
Module ex07

Adding a new record to the table
'''
from sqlite3 import connect

def main():
    name = input('Enter name: ')
    email = input('Enter email: ')
    phone = input('Enter phone: ')

    cmd = 'insert into contacts(name, email, phone) values(\'{}\', \'{}\', \'{}\')'.format(name, email, phone)

    conn = connect('philips_db.sqlite3')
    try: 
        c1 = conn.cursor()
        c1.execute(cmd)
        conn.commit()
        print('Data inserted!')
    except Exception as e:
        print('There was an error: ', e)
        conn.rollback()
        
    conn.close()

if __name__=='__main__': main()