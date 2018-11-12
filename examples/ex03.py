'''
Module ex03

Working with inheritance in Python
'''

class Person(object):

    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._email = kwargs.get('email')
        # print('Person.__init__() called')

    def __str__(self):
        return 'Person [Name={}, Email={}]'.format(self._name, self._email)

class Resource(object):
     
    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._location = kwargs.get('location')
        # print('Resource.__init__() called')

    def __str__(self):
        return 'Resource [Id={}, Location={}]'.format(self._id, self._location)

class Employee(Person, Resource):
    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        Person.__init__(self, **kwargs)
        Resource.__init__(self, **kwargs)

    def __str__(self):
        return 'Employee [Id={}, Name={}, email={}, Location={}]'.format(self._id, self._name, self._email, self._location)

def main():
    e1 = Employee(name='James', email='james@example.com', id=123, location='Bangalore')
    # print(dir(e1))
    
    print(e1)


if __name__=='__main__': main()