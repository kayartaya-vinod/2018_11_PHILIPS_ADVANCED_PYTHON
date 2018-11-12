'''
Module ex02

Working with Properties in class
'''

class Book(object):

    def __init__(self, **kwargs):
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        self.__author = kwargs.get('author')

    def __str__(self):
        return 'Book [Title={}, Price={}, Author={}]'.format(self.__title, self.__price, self.__author)

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if type(value) not in (int, float):
            raise TypeError('Invalid type for price; only int and float allowed')

        if value <= 0:
            raise ValueError('Invalid value for price; must be > 0')

        self.__price = value

    # __iadd__ correspond to the += operator
    # LHS of the operator is the invoking object
    # RHS is the value
    # also, this function must return the invoking object
    def __iadd__(self, value):
        if type(value) in (int, float):
            self.price += value
        elif type(value) == str:
            self.title += value
        return self
    # other operator functions:
    # __isub__, __imul__, __idiv__, __imod__ --> -=, *=, /=, %=
    # __add__, __sub__, __mul__, __div__, __mod__ --> + - * / %
    # __gt__, __ge__, __lt__, __le__, __eq__, __ne__ --> > >= < <= == !=

def main():
    b1 = Book(title='Let us C', author='Y Kanitkar', price=299)
    print(b1)

    print('Title  = ', b1.title)    # invokes the title() member function
    print('Author = ', b1.author)
    print('Price  = ', b1.price)

    # following is same as Book.title(b1, 'Let us Python')
    b1.title = 'Let us Python'
    b1.price = 123
    b1.author = 'Vinod K'

    print(b1)

    b1 += ' - 2nd edition'      # b1.title to be appended
    b1 += -15                    # b1.price to be added

    print(b1)

if __name__=='__main__': main()