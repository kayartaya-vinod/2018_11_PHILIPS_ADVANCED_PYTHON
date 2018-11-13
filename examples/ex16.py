'''
Module ex16

Comparison of function with/without thread
'''
import time
import threading

def calc_sum(filename, info):
    total = 0
    with open(filename) as file:
        for line in file:
            time.sleep(0.0005)
            try:
                total += float(line)
            except:
                pass
    info[filename] = total

def main():
    info = {}
    start_time = time.time()
    calc_sum('numbers1.txt', info)
    calc_sum('numbers2.txt', info)
    calc_sum('numbers3.txt', info)
    end_time = time.time()

    print(info)
    print('Total time taken is %s seconds' % (end_time-start_time))


class CalcSum(threading.Thread):
    def __init__(self, filename, info):
        threading.Thread.__init__(self)
        self.__filename = filename
        self.__info = info

    # a Thread class must override the run() ,
    # which is the first method executed in the thread's stack
    def run(self):
        total = 0
        with open(self.__filename) as file:
            for line in file:
                time.sleep(0.0005)
                try:
                    total += float(line)
                except:
                    pass
        self.__info[self.__filename] = total

def main_threads():
    info = {}
    start_time = time.time()
    t1 = CalcSum('numbers1.txt', info)
    t2 = CalcSum('numbers2.txt', info)
    t3 = CalcSum('numbers3.txt', info)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()
    print(info)
    print('Total time taken is %s seconds' % (end_time-start_time))

if __name__=='__main__': 
    main()
    main_threads()
