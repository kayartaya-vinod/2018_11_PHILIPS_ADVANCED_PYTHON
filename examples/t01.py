class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.city = kwargs.get('city')
        self.picture = kwargs.get('picture')

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        val = list(self.__dict__.keys())
        out = None

        if self.__index <len(val): out = val[self.__index]
        else: raise StopIteration
        self.__index +=1

        return out

def main():
    p1 = Person(name='vinod', city='bangalore', email='vinod@vinod.co',
        phone='9731424784', picture='vinod.png')

    for f in p1:
        print(f)

if __name__=='__main__': main()