'''
Module ex01

Example of creating and using classes in Python
'''

class Book(object):
    __publisher = 'KVinod Inc.'
    # __init__ is a special function automatically
    # called by Python when the object is newly constructed
    # and passes the reference of the same
    def __init__(self, **kwargs):
        # print('id of self is {}'.format(id(self)))
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        if kwargs.get('publisher') != None:
            self.__publisher = kwargs.get('publisher')

    # this is a user defined function, to be called using
    # an object's reference. ex: b1.print_info()
    # Python passes b1 to the function as first argument
    # implicitly (like Book.print_info(b1))
    def print_info(self):
        print('information about the book...')
        print('Title     =', self.__title)
        print('Price     =', self.__price)
        print('Publisher =', self.__publisher)
        print()

    def __str__(self):
        return 'Book [Title={}, Price={}, Publisher={}]'.format(self.__title, self.__price, self.__publisher)


def book_test():
    b1 = Book(title='Let us C', price=299, publisher='BPB')
    # print('id of b1 is {}'.format(id(b1)))
    # print('type of b1 is {}'.format(type(b1)))
    # b1.print_info()
    print(b1)
    # print('attributes of b1...')
    # print(dir(b1))

    b2 = Book()
    # b2.print_info()
    print(b2)

if __name__=='__main__':
    book_test()
