class Person(object):
    # class members are shared by objects
    # immutables like str, int, float will be changed
    # when the object changes its value
    name = ''
    email = ''
    # all instances of Person will use the same hobbies object
    hobbies = []

    def __init__(self, **kwargs):
        if 'name' in kwargs: self.name = kwargs['name']
        if 'email' in kwargs: self.email = kwargs['email']
        self.hobbies = []
        
    def addHobbie(self, hobbie):
        self.hobbies.append(hobbie)

def main():
    p1 = Person()
    p2 = Person()
    p3 = Person(name='vinod', email='vinod@vinod.co')

    p1.addHobbie('Golfing')
    p2.addHobbie('Fishing')

    print('p3\'s hobbies are: ', p3.hobbies)

    print('id of p1.name is', id(p1.name))
    print('id of p2.name is', id(p2.name))
    print('id of p3.name is', id(p3.name))

if __name__=='__main__': main()