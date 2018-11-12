'''
Module ex12

Model part of MVC 

Defines an entity class Contact and a 
Repository calss ContactDao
'''

class Contact(object):
    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__name = kwargs.get('name')
        self.__email = kwargs.get('email')
        self.__phone = kwargs.get('phone')
        self.__city = kwargs.get('city', 'Bangalore')
        self.__picture = kwargs.get('picture')

    def __str__(self):
        return 'Contact [Id={}, Name={}, Email={}, Phone={}, City={}, Picture={}]'.format(
            self.__id,
            self.__name,
            self.__email,
            self.__phone,
            self.__city,
            self.__picture
        )

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
        pass
    
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
        finally:
            self.__cleanup(conn, cur)
        
    
    def updateContact(self, contact):
        pass

    def deleteContact(self, id):
        pass

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
        finally:
            self.__cleanup(conn, cur)

    def getContactsByCity(self, city):
        pass

def main():
    dao = ContactsDao()
    c1 = dao.getContact(1)
    c2 = dao.getContact(10)

    # print('c1:', c1)
    # print('c2:', c2)

    contacts = dao.getAllContacts()

    for c in contacts:
        print(c)
    
if __name__=='__main__': main()