'''
Module ex10

Fetch all records from db table

Use these commands to create database, tables and rows

create database philips_db;
use philips_db;

create table contacts(
    id int primary key auto_increment,
    name varchar(50) not null,
    city varchar(50) default 'Bangalore',
    email varchar(100) unique,
    phone varchar(50) unique,
    picture varchar(255)
);

insert into contacts (name, email, phone) values
    ('Vinod', 'vinod@vinod.co', '9731424784'),
    ('Shyam', 'shyam@example.com', '9872278965');
    
insert into contacts (name, email, phone, city) values
    ('John', 'johndoe@example.com', '5559281122', 'Dallas');

'''
from pymysql import connect

def main():

    props = {}
    props['user'] = 'root'
    props['password'] = 'root'
    props['host'] = 'localhost'
    props['port'] = 3306
    props['database'] = 'philips_db'

    conn = connect(**props)

    cur = conn.cursor()
    cur.execute('select * from contacts where city = %s', ('Bangalore',))
    data = cur.fetchall()
    if len(data) > 0:
        for rec in data:
            print(rec)
    else:
        print('No data found!')

if __name__=='__main__': main()