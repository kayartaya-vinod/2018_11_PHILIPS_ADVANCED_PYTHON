'''
Module ex15

A very basic Thread example
'''

from time import sleep
import threading

def print_numbers(name, start=1, end=10, skip=1):
    for i in range(start, end+1, skip):
        print('In thread "%s" value of i is %d' % (name, i))
        sleep(.5)

def main():
    print('main() started!')
    t1 = threading.Thread(target=print_numbers, args=('first', 5))
    t2 = threading.Thread(target=print_numbers, args=('second',))
    t1.start() # DOES NOT call the run() of Thread class
    t2.start() # DOES NOT call the run() of Thread class

    t1.join()
    t2.join()
    print('main() ended!')

if __name__=='__main__': main()