'''
Module ex12

Model part of MVC 

Defines an entity class Contact and a 
Repository calss ContactDao
'''

import json

class Contact(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.city = kwargs.get('city', 'Bangalore')
        self.picture = kwargs.get('picture')

    def __str__(self):
        return 'Contact [Id={}, Name={}, Email={}, Phone={}, City={}, Picture={}]'.format(
            self.id,
            self.name,
            self.email,
            self.phone,
            self.city,
            self.picture
        )

    @property
    def as_json(self):
        return json.dumps(self.__dict__)

    @as_json.setter
    def as_json(self, value):
        self.__dict__ = json.loads(value)


class DaoException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class ContactsDao(object):

    def __getCursor(self):
        from sqlite3 import connect
        conn = connect('philips_db.sqlite3')
        cur = conn.cursor()
        return (conn, cur)

    def __cleanup(self, conn, cur):
        cur.close()
        conn.close()

    def __getContact(self, data):
        return Contact(
                id = data[0],
                name = data[1],
                city = data[2],
                email = data[3],
                phone = data[4],
                picture = data[5]
            )

    def addContact(self, contact):
        if type(contact)!=Contact: 
            raise TypeError('Only Contact instance is allowed')

        conn, cur = self.__getCursor()
        try:
            sql = 'insert into contacts(name, city, email, phone, picture) values(?,?,?,?,?)'
            cur.execute(sql, (contact.name, contact.city, contact.email, contact.phone, contact.picture))
            contact.id = cur.lastrowid
            conn.commit()
            return contact
        except Exception as e:
            raise DaoException('There was an error: {}'.format(e))
        finally:
            self.__cleanup(conn, cur)
    
    def getContact(self, id=None):
        '''
        This method accepts an int id and returns an instance
        of Contact class with the given id, searched and obtained
        from the database table 'contacts'. If not found, None is
        returned
        '''
        if id==None or type(id) != int:
            raise ValueError('id is required and must be int')

        conn, cur = self.__getCursor()
        try:
            cur.execute('select * from contacts where id = ?', (id,))
            data = cur.fetchone()
            if data==None: return None
            
            return self.__getContact(data)
        except Exception as e:
            raise DaoException('There was an error: {}'.format(e))
        finally:
            self.__cleanup(conn, cur)
        
    
    def updateContact(self, contact):
        conn, cur = self.__getCursor()
        try:
            sql = 'update contacts set name=?, city=?, email=?, phone=?, picture=? where id=?'
            cur.execute(sql, (contact.name, contact.city, contact.email, contact.phone, contact.picture, contact.id))
            conn.commit()
            return contact
        except Exception as e:
            raise DaoException('There was an error: {}'.format(e))
        finally:
            self.__cleanup(conn, cur)
    

    def deleteContact(self, id):
        if id==None or type(id) != int:
            raise ValueError('id is required and must be int')

        conn, cur = self.__getCursor()
        try:
            cur.execute('delete from contacts where id = ?', (id,))
            conn.commit()
            
        except Exception as e:
            raise DaoException('There was an error: {}'.format(e))
        finally:
            self.__cleanup(conn, cur)

    def getAllContacts(self):
        '''
        should return a tuple of contact instances for all records
        '''
        conn, cur = self.__getCursor()
        try:
            cur.execute('select * from contacts')
            data = cur.fetchall()
            
            lst = []
            for d in data: lst.append(self.__getContact(d))
            
            return lst
        except Exception as e:
            raise DaoException('There was an error: {}'.format(e))
        finally:
            self.__cleanup(conn, cur)

    def getContactsByCity(self, city):
        conn, cur = self.__getCursor()
        try:
            cur.execute('select * from contacts where city=?', (city,))
            data = cur.fetchall()
            
            lst = []
            for d in data: lst.append(self.__getContact(d))
            
            return lst
        finally:
            self.__cleanup(conn, cur)

def main():
    dao = ContactsDao()
    c1 = dao.getContact(1)
    c2 = dao.getContact(10)

    # print('c1:', c1)
    # print('c2:', c2)

    contacts = dao.getAllContacts()

    for c in contacts:
        print(c)

    # c3 = Contact(name='Rajesh', email='rajesh@xmple.com', city='Bangalore', phone='938373234')
    # c3 = dao.addContact(c3)
    # print('After adding, c3 is: ', c3)
    
if __name__=='__main__': main()